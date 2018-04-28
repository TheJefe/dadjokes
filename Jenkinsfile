node {
    git 'git@github.com:TheJefe/dadjokes.git'

    stage('Test') {
        def testImage = docker.build("thejefe/dadjokes", "-f Dockerfile.build .")
        testImage.inside('-u root') {
            sh 'pip install -r requirements.txt && ./manage.py test'
        }
    }

    stage('Deploy') {
        def cleanImage = docker.build("thejefe/dadjokes")
        cleanImage.push('latest')
    }
}
