## Argo Webhook config:

PoC

Helm:
Use the chart in `chart` folder.



Manual configuration:

1. Create application in Argo CD - Use the ui 
See manifiest in application.yml

2. Install Argo CD Notifications 

```
k apply -n cre-system -f https://raw.githubusercontent.com/argoproj-labs/argocd-notifications/stable/manifests/install.yaml
```

3. Install Configmap: use command in cm.yml

4. Install Secret: use command in secret.yml

5. synchronize app


k patch app se-enablers-dev -n cre-system -p '{"metadata": {"annotations": {"recipients.argocd-notifications.argoproj.io":"webhook:devhose"}}}' --type merge


k exec -it kubernetes-bootcamp-75bccb7d87-zxng2 -- /bin/bash



helm2 install --repo https://github.com/argoproj/argo-helm/tree/master/charts/argocd-notifications mynotifications 

devhose.mpi-internal.com


helm2 del --purge mynotifier
helm2 install -n mynotifier .