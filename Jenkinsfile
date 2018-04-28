pipeline {
    agent any
    // git 'git@github.com:TheJefe/dadjokes.git'

    stages {
        stage('Test') {
            steps {
                sh '''#!/bin/bash -l
                pip install -r requirements.txt
                ./manage.py test
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // docker build -t thejefe/dadjokes .
                // docker push thejefe/dadjokes
            }
        }
    }
}
