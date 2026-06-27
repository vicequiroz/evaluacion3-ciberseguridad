pipeline {
    agent any

    stages {
        stage('1. Construccion') {
            steps {
                echo 'Iniciando fase de construcción segura de la aplicación...'

                sh 'python3 --version'

                echo 'Creando entorno virtual e instalando dependencias...'
                sh '''
                    rm -rf venv
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''

                echo 'Verificando archivos del proyecto...'
                sh 'ls -lh'
            }
        }

        stage('2. Pruebas') {
            steps {
                echo 'Levantando aplicación Flask para pruebas locales...'

                sh '''
                    pkill -f "python app.py" || true
                    nohup ./venv/bin/python app.py > flask.log 2>&1 &
                    sleep 5

                    echo "Probando acceso a la aplicación:"
                    curl http://localhost:5000
                '''
            }
        }

        stage('3. OWASP ZAP') {
            steps {
                echo 'Iniciando análisis automatizado de seguridad DAST con OWASP ZAP...'

                sh '''
                    docker run --rm --network host \
                    ghcr.io/zaproxy/zaproxy:stable \
                    zap-baseline.py -t http://localhost:5000 || true
                '''
            }
        }

        stage('4. Despliegue') {
            steps {
                echo 'Iniciando etapa de despliegue de la aplicación...'

                sh '''
                    mkdir -p deploy
                    rm -rf deploy/*

                    cp app.py deploy/
                    cp requirements.txt deploy/

                    echo "Proyecto desplegado correctamente en carpeta deploy."
                    ls -lh deploy/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline CI/CD finalizado correctamente: construcción, pruebas, OWASP ZAP y despliegue exitosos.'
        }

        failure {
            echo 'El pipeline falló. Revisar errores en la consola de Jenkins.'
        }
    }
}
