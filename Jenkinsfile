pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh "rm tests/test_int*"
                sh "bash test.sh"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}