pipeline {
    agent any

    stages {
        stage('1. Construccion') {
            steps {
                echo 'Construyendo aplicación Flask...'
                sh 'python3 --version'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh 'ls -l'
            }
        }

        stage('2. Pruebas') {
            steps {
                echo 'Ejecutando aplicación Flask para pruebas...'
                sh '''
                    pkill -f "python app.py" || true
                    nohup ./venv/bin/python app.py > flask.log 2>&1 &
                    sleep 5
                    curl http://localhost:5000
                '''
            }
        }

        stage('3. OWASP ZAP') {
            steps {
                echo 'Ejecutando análisis automatizado de seguridad con OWASP ZAP...'
                sh '''
                    docker run --rm --network host \
                    -v $(pwd):/zap/wrk/:rw \
                    ghcr.io/zaproxy/zaproxy:stable \
                    zap-baseline.py -t http://localhost:5000 -r zap_report.html || true
                '''
            }
        }

        stage('4. Despliegue') {
            steps {
                echo 'Desplegando aplicación Flask...'
                sh '''
                    mkdir -p deploy
                    rm -rf deploy/*
                    cp app.py deploy/
                    cp requirements.txt deploy/
                    ls -l deploy/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline finalizado correctamente con pruebas de seguridad OWASP ZAP.'
        }
        failure {
            echo 'El pipeline falló. Revisar errores en la consola.'
        }
    }
}
