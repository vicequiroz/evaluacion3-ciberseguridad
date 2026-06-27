pipeline {
    agent any

    stages {
        stage('1. Construccion') {
            steps {
                echo 'Descargando el código más reciente desde GitHub...'
                checkout scm

                echo 'Verificando versión de Python...'
                sh 'python3 --version'

                echo 'Verificando archivos del proyecto...'
                sh 'ls -l'
            }
        }

        stage('2. Pruebas') {
            steps {
                echo 'Ejecutando prueba de la aplicación Python...'
                sh 'python3 app.py'
            }
        }

        stage('3. Despliegue') {
            steps {
                echo 'Iniciando el despliegue interno...'
                sh '''
                    echo "Creando el directorio de despliegue si no existe..."
                    mkdir -p /var/jenkins_home/deploy

                    echo "Limpiando despliegues anteriores..."
                    rm -rf /var/jenkins_home/deploy/*

                    echo "Copiando app.py al directorio de destino..."
                    cp app.py /var/jenkins_home/deploy/

                    echo "Verificando archivo desplegado:"
                    ls -l /var/jenkins_home/deploy/

                    echo "Ejecutando aplicación desde el despliegue:"
                    python3 /var/jenkins_home/deploy/app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline CI/CD finalizado correctamente: construcción, pruebas y despliegue exitosos.'
        }
        failure {
            echo 'El pipeline falló. Revisar errores en la consola de Jenkins.'
        }
    }
}
