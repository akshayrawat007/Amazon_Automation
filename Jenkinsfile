pipeline {

agent any

parameters {
    choice(
        name: 'TEST_SUITE',
        choices: ['all', 'sanity', 'regression', 'smoke'],
        description: 'Select test suite to run'
    )
    string(
        name: 'TEST_FILE',
        defaultValue: '',
        description: 'Run specific test file (e.g. tests/test_login.py). Leave blank to use TEST_SUITE.'
    )
    booleanParam(
        name: 'HEADLESS',
        defaultValue: true,
        description: 'Run browser in headless mode'
    )
}

environment {
    HEADLESS = "${params.HEADLESS}"
}

stages {

    stage('Checkout Code') {
        steps {
            git(
                url: 'https://github.com/akshayrawat007/Amazon_Automation.git',
                branch: 'main',
                credentialsId: 'github_1'
            )
        }
    }

    stage('Prepare Environment') {
        steps {
            withCredentials([
                file(credentialsId: 'amazon-env-file', variable: 'ENV_FILE'),
                file(credentialsId: 'GOOGLE_SERVICE_ACCOUNT', variable: 'GOOGLE_JSON')
            ]) {
                bat 'copy "%ENV_FILE%" .env'
                bat 'copy "%GOOGLE_JSON%" service-account.json'
            }
        }
    }

    stage('Install Dependencies') {
        steps {
            bat 'pip install -r requirements.txt'
        }
    }

    stage('Run Tests') {
        steps {
            script {
                def target = params.TEST_FILE?.trim()
                    ? params.TEST_FILE.trim()
                    : (params.TEST_SUITE == 'all'
                        ? 'tests/'
                        : "tests/ -m ${params.TEST_SUITE}")

                bat "pytest ${target} --alluredir=reports/allure-results"
            }
        }
    }
}

post {
    always {
        allure([
            includeProperties: false,
            jdk: '',
            results: [[path: 'reports/allure-results']]
        ])
    }

    success {
        echo 'Tests passed successfully'
    }

    failure {
        echo 'Tests failed — check Allure report'
    }
}

}
