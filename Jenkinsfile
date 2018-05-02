node {
    def cluster = 'dadjokes'
    def service = 'dadjokes'
    def region = 'us-east-1'
    git 'git@github.com:TheJefe/dadjokes.git'

    stage('Test') {
        def testImage = docker.build("thejefe/dadjokes", "-f Dockerfile.build .")
        testImage.inside('-u root') {
            sh 'pip install -r requirements.txt && ./manage.py test'
        }
    }

    stage('Publish') {
        withDockerRegistry([credentialsId: 'c106fdf4-34ae-47a7-80e5-ffaca4a6f25f']) {
            def cleanImage = docker.build("thejefe/dadjokes")
            if (BRANCH_NAME == 'master') {
                cleanImage.push('latest')
            }
            cleanImage.push(BRANCH_NAME)
        }
    }

    stage('Deploy') {
        if (BRANCH_NAME == 'master') {
            @Library('jenkins-shared-library')
            def ecs = new ecs()
            ecs.deployService(cluster, service, region)
        } else {
            echo 'No deployments for non-master branches'
        }
    }
}
