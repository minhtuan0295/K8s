pipeline {
    agent any 
    stages {
        stage ('Build docker image'){
            steps {
                sh 'docker build . -t my-python-app-image:latest'
            }
        }
        stage ('Run container and expose its port 10000'){
            steps {
                sh 'docker run -d -p 10000:10000 --name my-python-server-container my-python-app-image:latest'
            }
        }
    }
}


// node {
//     // agent {
//     //     dockerfile true
//     // }
//     // stages {
//     //     stage('Build docker image') {
//     //         steps {
//     //             echo 'Start running web server in docker container'
//     //         } 
//     //     }
//     // }
//     def my_app
//     stage('Build image') {
//         checkout scm
//         my_app = docker.build('my-python-app-image:latest')
//         my_app.run('my-python-app-image:latest', "-d -p 10000:10000")
//     }
//     stage('Start server in docker container') {
//         my_app.inside {
//             sh 'python server_app.py'
//         }
//     }
// }