pipeline{
        agent any
        stages{
          stage('---Build_Image---'){
                          steps{
                              sh "sudo docker build -t charagen -f ./character_sheets/Dockerfile ."
                         }
                  }
                  stage('---clean---'){
                          steps{
                                sh label: '', script: '''if [ ! "$(sudo docker ps -q -f name=charagen)" ]; then
                if [ "$(sudo docker ps -aq -f status=exited -f name=charagen)" ]; then
                  # cleanup
                  sudo docker rm -f charagen
                fi
            fi'''
                          }
                  }
          stage('----run----'){
              steps{
                  sh 'sudo docker run -d --name charagen -p 8888:8888 charagen'
              }
          }
        }
}
