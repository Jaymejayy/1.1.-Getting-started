# Exercise 2.3 – Namespaces

## Overview

Created a Kubernetes namespace called `exercises` to separate exercise applications from the default namespace.

## Changes made

- Created the `exercises` namespace.
- Moved the **Log output** application into the `exercises` namespace.
- Moved the **Ping-pong** application into the `exercises` namespace.
- Updated their Deployment, Service, and Ingress manifests with `namespace: exercises`.
- Created a PersistentVolumeClaim named `shared-data-claim` in the `exercises` namespace so Log output can continue using persistent storage.
- Applied the updated manifests and verified that both applications were running in the new namespace.
- Removed the old Log output and Ping-pong resources from the `default` namespace.

## Verification

Both applications were confirmed running in the `exercises` namespace:

- `log-output-dep`
- `ping-pong-dep`

Their Services and shared Ingress were also created in the `exercises` namespace.
