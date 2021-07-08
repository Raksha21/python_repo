pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "I'm running with jenkins"
                    ls -lah
                '''
            }
        }
    }
}
