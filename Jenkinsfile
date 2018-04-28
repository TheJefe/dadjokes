node {
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
            cleanImage.push('latest')
        }
    }
}
