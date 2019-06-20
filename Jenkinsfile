pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = '833755589:AAFUuTYH5RCDW8IC7xkuHL0Nvk_X8Z7odAY'
        TELEGRAM_CHAT_ID = '-1001376102301'
        SONAR_PROJECT_KEY = 'ua.com.smiddle:SmiddleManager'
        SONAR_HOST_URL = 'http://10.100.70.7:9090'
        SONAR_PROXY_URL = 'https://dev.smiddle.com'
        SONAR_LOGIN = '7d8d530419f264cb8632ca950b45fb310e2e162a'
    }

    stages {
        stage('image') {
            steps {
                notification("_Started_ 😱 : *${env.JOB_NAME}* \nBranch - ${env.GIT_BRANCH} by ${env.GIT_AUTHOR} \n[Jenkins](${env.BUILD_URL})")
                docker.build "latest"
            }
        }
    }
    post {
        failure {
            notification("🤖 _Failed_ 💩 : *${env.JOB_NAME}* - ${env.BUILD_NUMBER} after ${currentBuild.durationString} \n [Jenkins](${env.BUILD_URL})")
        }
        success {
            notification("🤖 _Success_ 👍 : *${env.JOB_NAME}* - ${env.BUILD_NUMBER} after ${currentBuild.durationString} \n[Jenkins](${env.BUILD_URL})")
        }
    }
}

void notification(GString message) {
    sh "curl " +
            "--data-urlencode chat_id=${env.TELEGRAM_CHAT_ID} " +
            "--data-urlencode text=\"${message}\" " +
            "--data-urlencode parse_mode=Markdown " +
            "https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage"
}