pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-credentials-id'
        KUBECONFIG_CREDENTIALS_ID = 'kubeconfig-credentials-id'
        DOCKER_REGISTRY = 'https://index.docker.io/v1/'
        DOCKER_REPO = 'docker-repo'
        BUILD_TAG = "build-${env.BUILD_ID}"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/equqe/mezhgortrans.git'
            }
        }

        stage('Build & Push Docker Images') {
            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDENTIALS_ID) {
                        def coreImage = docker.build("${DOCKER_REPO}/core:${BUILD_TAG}")
                        coreImage.push()
                    }
                }
            }
        }

        stage('Update Manifests') {
            steps {
                script {
                    sh """
                    sed -i 's|build-\${BUILD_ID}|${BUILD_TAG}|g' k8s-manifests/core-deployment.yml
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withCredentials([file(credentialsId: KUBECONFIG_CREDENTIALS_ID, variable: 'KUBECONFIG')]) {
                        sh 'kubectl --kubeconfig=$KUBECONFIG apply -f k8s-manifests/core-deployment.yml'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
