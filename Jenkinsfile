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
        sh '''./scripts/testScript.sh
echo "Dammit"'''
      }
    }
    stage('Failing script (on purpose)') {
      steps {
        sh './scripts/testScriptFail.sh'
      }
    }
  }
}