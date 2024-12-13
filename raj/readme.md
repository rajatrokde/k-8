helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
helm install sonarqube sonarqube/sonarqube --namespace sonarqube --create-namespace
