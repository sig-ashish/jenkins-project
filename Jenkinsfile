pipeline {
  agent any
  environment {
    registry = "ashishsigmoid/jenkins-assignment"
    registryCredential = 'docker_hub_id'
    dockerImage = ''
    IMAGE_REPO_NAME="jenkins-assignment"
    IMAGE_TAG="v1"
  }
  stages {
    stage('Cloning Git') {
      steps {
        script {
          checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/sig-ashish/jenkins-project.git']]])

          }    
        }
      }
    stage('Building Image') {
      steps{
        script {
          dockerImage = docker.build "ashishsigmoid/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
        }
      }
    }
    stage('Push image') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'docker_hub_id', passwordVariable: 'DOCKER_PSWD', usernameVariable: 'DOCKER_USER')]) {
            sh 'docker login -u ashishsigmoid -p ${DOCKER_PSWD}'
            sh "docker push ashishsigmoid/jenkins-assignment:v1"
}
            
        }
      }
    }
    stage('Deploying') {
      steps {
            withCredentials([kubeconfigFile(credentialsId: 'k8s', variable: 'KUBECRED')]) {
                    sh 'cat $KUBECRED > ~/.kube/config'
                    echo "Deploying to cluster"
                    sh 'docker pull ashishsigmoid/jenkins-assignment:v1'
                    sh '/usr/local/bin/kubectl create -f deployment.yaml'
        // sh 'docker pull ashishsigmoid/jenkins-assignment:v1'
        // sh '/usr/local/bin/kubectl create -f deployment.yaml -f service.yaml'
        
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




