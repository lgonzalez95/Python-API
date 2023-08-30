pipeline {
    agent any

    parameters{
        choice(
            choices: ['dev', 'qa'], 
            name: 'Environment',
            description: 'Select the required environment'
        )
        string(
            name: 'Marks', 
            defaultValue: '', 
            description: 'Enter the python marks to run'
        )
    }

    environment {
        ENV = "${params.Environment}"
        DB_USER = credentials('DB_USER')
        DB_PASSWORD = credentials('DB_PASSWORD')
        WORKSPACE = env.WORKSPACE
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
