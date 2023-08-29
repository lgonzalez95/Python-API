pipeline {
    agent any

    parameters{
        choice(
            choices: ['dev', 'qa'], 
            name: 'Environment',
            description: 'Select the required environment'
        )
        text(
            name: 'Marks', 
            defaultValue: '', 
            description: 'Enter the python marks to run'
        )
    }

    stages {
        stage('Setup'){
            steps{
                echo "SETUP"
            }
        }

        stage('Build Cypress Image') {
            steps {
                sh "docker build -t api-test-runner ."
            }
        }

        stage('Run Tests') {
            steps{
                sh "docker-compose up --force-recreate"
            }
            post {
                cleanup {
                    sh "docker-compose down"
                }
            } 
        }
    }
}
