pipeline {
    agent any

    environment {
        // ✅ Put your real Docker Hub username here
        DOCKERHUB_USER = 'akshitavidiyala'
        // ✅ Name of your Docker Hub repo (create this on Docker Hub if not already)
        IMAGE_NAME = 'exp9dev'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                echo "Building Docker image: ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo "Logging in to Docker Hub as ${DOCKER_USER}"
                    echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh """
                echo "Tagging image as latest"
                docker tag ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest

                echo "Pushing image tags to Docker Hub..."
                docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}
                docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f || true'
        }
        success {
            echo "✅ Build and push successful!"
        }
        failure {
            echo "❌ Build or push failed. Check console output."
        }
    }
}

