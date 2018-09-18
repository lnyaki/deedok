pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Test pipeline. Does it even work?'
      }
    }
    stage('Execute script') {
      steps {
        sh '''./testScript.sh
echo "Dammit"'''
      }
    }
  }
}