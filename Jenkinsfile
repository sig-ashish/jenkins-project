pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="708543810688"
        AWS_DEFAULT_REGION="ap-south-1" 
        IMAGE_REPO_NAME="jenkins-assignment"
        IMAGE_TAG="v1"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
       
    }
   
    stages {
        
         stage('Logging into AWS ECR') {
            steps {
                script {
                sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
                 
            }
        }
        
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/sig-ashish/jenkins-project.git']]])     
            }
        }
  
    // Building Docker images
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
        }
      }
    }
   
    // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
     steps{  
         script {
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
         }
        }
      }
stage('Deploying') {
      steps {
        script {
          kubeconfig(credentialsId: 'k8s_id', serverUrl: 'https://192.168.1.10:8443') {
            try {
              sh "kubectl create -f deployment.yaml"
              echo "Successfully Deployed."
              sh "kubectl get pods"
              sh "kubectl get deployments"
              
            }
}
}
}
}
      

        stage('list of images in ECR, pods and deployments in EKS') {
            steps{  
                script {
                    echo "Showing list of ECR, pods and deployments in EKS"
                    echo "List of images in ECR"
                    sh "aws ecr list-images --repository-name jenkins-assignment"
                    echo "List of pods"
                    sh "/usr/local/bin/kubectl get pods"
                    echo "List of deployment"
                    sh "/usr/local/bin/kubectl get deploy"
                }
            }
       }
       
    }
        
    
post {
        always {
            emailext body: '''$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS:

Check console output at $BUILD_URL to view the results.''', subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', to: 'ashishyadav@sigmoidanalytics.com'
        }
    }
}
