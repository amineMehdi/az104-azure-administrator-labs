# Lab 16 answer key and remediation

[Return to the questions](./QUESTIONS.md) · [Return to the guided lab](../README.md)

Score one point per correct response:

- **43–50 (85–100%): Mastery.** Continue to the next lab and revisit these tasks during final review.
- **35–42 (70–84%): Targeted review.** Repeat the linked tasks for every missed question.
- **0–34 (below 70%): Rebuild.** Repeat the complete lab, including validation and break/fix, before retrying.

## LAB16-Q01 — B

**Question:** A new web hardening operator must explain why the hardened and recoverable web application can reject inbound clients that negotiate a protocol below the approved TLS version. Which explanation is accurate?

- **A — Incorrect.** Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
  Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate. In the hardened and recoverable web application, this statement describes HTTPS-only redirection. Hardened and recoverable web application asks about minimum inbound TLS; this HTTPS-only redirection choice leaves the minimum inbound TLS explanation missing.
- **B — Correct.** The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
  The hardened and recoverable web application needs minimum inbound TLS to reject inbound clients that negotiate a protocol below the approved TLS version; this option states the applicable minimum inbound TLS rule: the App Service minimum TLS setting rejects client handshakes below the configured protocol version.
- **C — Incorrect.** App Service requires proof of custom-domain ownership before binding the hostname.
  App Service requires proof of custom-domain ownership before binding the hostname. In the hardened and recoverable web application, this statement describes domain ownership verification. Selecting domain ownership verification for hardened and recoverable web application leaves minimum inbound TLS unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a minimum inbound TLS basis to reject inbound clients that negotiate a protocol below the approved TLS version.
- **D — Incorrect.** App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
  App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private. In the hardened and recoverable web application, this statement describes regional VNet integration. Minimum inbound TLS governs hardened and recoverable web application; regional VNet integration cannot support minimum inbound TLS when operators must reject inbound clients that negotiate a protocol below the approved TLS version.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q02 — B

**Question:** The hardened and recoverable web application acceptance criteria require operators to redirect unencrypted application requests to HTTPS. Which service fact supports that requirement?

- **A — Incorrect.** An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
  An App Service managed certificate can cover eligible custom domains but has feature and validation limitations. In the hardened and recoverable web application, this statement describes App Service managed certificates. The App Service managed certificates statement accurately describes App Service managed certificates; however, hardened and recoverable web application needs HTTPS-only redirection to redirect unencrypted application requests to HTTPS; App Service managed certificates cannot replace HTTPS-only redirection.
- **B — Correct.** Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
  Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate. This HTTPS-only redirection fact resolves the hardened and recoverable web application design question about how to redirect unencrypted application requests to HTTPS.
- **C — Incorrect.** App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
  App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data. In the hardened and recoverable web application, this statement describes App Service backup storage. HTTPS-only redirection governs hardened and recoverable web application; App Service backup storage cannot support HTTPS-only redirection when operators must redirect unencrypted application requests to HTTPS.
- **D — Incorrect.** An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
  An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution. In the hardened and recoverable web application, this statement describes App Service private endpoints. Hardened and recoverable web application asks about HTTPS-only redirection; this App Service private endpoints choice leaves the HTTPS-only redirection explanation missing.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q03 — B

**Question:** A web hardening reviewer challenges whether the hardened and recoverable web application can bind a supported platform-managed certificate to a custom hostname. Which response resolves the concern?

- **A — Incorrect.** A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
  A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records. In the hardened and recoverable web application, this statement describes custom-domain DNS records. Selecting custom-domain DNS records for hardened and recoverable web application leaves App Service managed certificates unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a App Service managed certificates basis to bind a supported platform-managed certificate to a custom hostname.
- **B — Correct.** An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
  An App Service managed certificate can cover eligible custom domains but has feature and validation limitations. For hardened and recoverable web application, App Service managed certificates supplies the service rule needed to bind a supported platform-managed certificate to a custom hostname.
- **C — Incorrect.** The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
  The backup schedule controls frequency and retention, subject to App Service tier and platform limits. In the hardened and recoverable web application, this statement describes backup schedules and retention. Hardened and recoverable web application asks about App Service managed certificates; this backup schedules and retention choice leaves the App Service managed certificates explanation missing.
- **D — Incorrect.** Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
  Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app. In the hardened and recoverable web application, this statement describes App Service access restrictions. The App Service access restrictions statement accurately describes App Service access restrictions; however, hardened and recoverable web application needs App Service managed certificates to bind a supported platform-managed certificate to a custom hostname; App Service access restrictions cannot replace App Service managed certificates.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q04 — D

**Question:** The hardened and recoverable web application handoff omits the web hardening rule needed to publish the record type required for the chosen custom hostname. Which statement should the team add?

- **A — Incorrect.** App Service requires proof of custom-domain ownership before binding the hostname.
  App Service requires proof of custom-domain ownership before binding the hostname. In the hardened and recoverable web application, this statement describes domain ownership verification. Custom-domain DNS records governs hardened and recoverable web application; domain ownership verification cannot support custom-domain DNS records when operators must publish the record type required for the chosen custom hostname.
- **B — Incorrect.** App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
  App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private. In the hardened and recoverable web application, this statement describes regional VNet integration. Hardened and recoverable web application asks about custom-domain DNS records; this regional VNet integration choice leaves the custom-domain DNS records explanation missing.
- **C — Incorrect.** The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
  The App Service minimum TLS setting rejects client handshakes below the configured protocol version. In the hardened and recoverable web application, this statement describes minimum inbound TLS. The minimum inbound TLS statement accurately describes minimum inbound TLS; however, hardened and recoverable web application needs custom-domain DNS records to publish the record type required for the chosen custom hostname; minimum inbound TLS cannot replace custom-domain DNS records.
- **D — Correct.** A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
  A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records. In the hardened and recoverable web application, this custom-domain DNS records rule supports the need to publish the record type required for the chosen custom hostname.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q05 — D

**Question:** A web hardening incident review of the hardened and recoverable web application depends on the ability to prove control of a hostname before binding it to the application. Which platform description is reliable?

- **A — Incorrect.** App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
  App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data. In the hardened and recoverable web application, this statement describes App Service backup storage. Hardened and recoverable web application asks about domain ownership verification; this App Service backup storage choice leaves the domain ownership verification explanation missing.
- **B — Incorrect.** An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
  An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution. In the hardened and recoverable web application, this statement describes App Service private endpoints. The App Service private endpoints statement accurately describes App Service private endpoints; however, hardened and recoverable web application needs domain ownership verification to prove control of a hostname before binding it to the application; App Service private endpoints cannot replace domain ownership verification.
- **C — Incorrect.** Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
  Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate. In the hardened and recoverable web application, this statement describes HTTPS-only redirection. Selecting HTTPS-only redirection for hardened and recoverable web application leaves domain ownership verification unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a domain ownership verification basis to prove control of a hostname before binding it to the application.
- **D — Correct.** App Service requires proof of custom-domain ownership before binding the hostname.
  For the hardened and recoverable web application, the rule for domain ownership verification is defined by this statement: app Service requires proof of custom-domain ownership before binding the hostname. It supports the required outcome to prove control of a hostname before binding it to the application.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q06 — D

**Question:** An application-platform administrator hardening and protecting a web app is updating the web hardening runbook. The requirement is to write application backups to an authorized storage destination. Which statement describes Azure behavior correctly?

- **A — Incorrect.** The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
  The backup schedule controls frequency and retention, subject to App Service tier and platform limits. In the hardened and recoverable web application, this statement describes backup schedules and retention. The backup schedules and retention statement accurately describes backup schedules and retention; however, hardened and recoverable web application needs App Service backup storage to write application backups to an authorized storage destination; backup schedules and retention cannot replace App Service backup storage.
- **B — Incorrect.** Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
  Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app. In the hardened and recoverable web application, this statement describes App Service access restrictions. Selecting App Service access restrictions for hardened and recoverable web application leaves App Service backup storage unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a App Service backup storage basis to write application backups to an authorized storage destination.
- **C — Incorrect.** An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
  An App Service managed certificate can cover eligible custom domains but has feature and validation limitations. In the hardened and recoverable web application, this statement describes App Service managed certificates. App Service backup storage governs hardened and recoverable web application; App Service managed certificates cannot support App Service backup storage when operators must write application backups to an authorized storage destination.
- **D — Correct.** App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
  App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data. The hardened and recoverable web application applies that App Service backup storage boundary when operators must write application backups to an authorized storage destination.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q07 — A

**Question:** A web hardening peer review asks how the hardened and recoverable web application should handle this outcome: retain scheduled backups for the required recovery window. Which explanation is accurate?

- **A — Correct.** The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
  The hardened and recoverable web application needs backup schedules and retention to retain scheduled backups for the required recovery window; this option states the applicable backup schedules and retention rule: the backup schedule controls frequency and retention, subject to App Service tier and platform limits.
- **B — Incorrect.** App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
  App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private. In the hardened and recoverable web application, this statement describes regional VNet integration. Backup schedules and retention governs hardened and recoverable web application; regional VNet integration cannot support backup schedules and retention when operators must retain scheduled backups for the required recovery window.
- **C — Incorrect.** The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
  The App Service minimum TLS setting rejects client handshakes below the configured protocol version. In the hardened and recoverable web application, this statement describes minimum inbound TLS. Hardened and recoverable web application asks about backup schedules and retention; this minimum inbound TLS choice leaves the backup schedules and retention explanation missing.
- **D — Incorrect.** A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
  A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records. In the hardened and recoverable web application, this statement describes custom-domain DNS records. The custom-domain DNS records statement accurately describes custom-domain DNS records; however, hardened and recoverable web application needs backup schedules and retention to retain scheduled backups for the required recovery window; custom-domain DNS records cannot replace backup schedules and retention.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q08 — D

**Question:** For the hardened and recoverable web application, the web hardening plan must send outbound application traffic into an approved regional virtual network. Which statement about web hardening belongs in the hardened and recoverable web application record?

- **A — Incorrect.** An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
  An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution. In the hardened and recoverable web application, this statement describes App Service private endpoints. Regional VNet integration governs hardened and recoverable web application; App Service private endpoints cannot support regional VNet integration when operators must send outbound application traffic into an approved regional virtual network.
- **B — Incorrect.** Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
  Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate. In the hardened and recoverable web application, this statement describes HTTPS-only redirection. Hardened and recoverable web application asks about regional VNet integration; this HTTPS-only redirection choice leaves the regional VNet integration explanation missing.
- **C — Incorrect.** App Service requires proof of custom-domain ownership before binding the hostname.
  App Service requires proof of custom-domain ownership before binding the hostname. In the hardened and recoverable web application, this statement describes domain ownership verification. The domain ownership verification statement accurately describes domain ownership verification; however, hardened and recoverable web application needs regional VNet integration to send outbound application traffic into an approved regional virtual network; domain ownership verification cannot replace regional VNet integration.
- **D — Correct.** App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
  App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private. This regional VNet integration fact resolves the hardened and recoverable web application design question about how to send outbound application traffic into an approved regional virtual network.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Integrate an App Service app with an Azure virtual network](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Source reviewed:** 2026-08-31

## LAB16-Q09 — B

**Question:** The web hardening review compares four claims for the hardened and recoverable web application requirement to give the application an inbound private address without making integration bidirectional. Which claim is technically sound?

- **A — Incorrect.** Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
  Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app. In the hardened and recoverable web application, this statement describes App Service access restrictions. Hardened and recoverable web application asks about App Service private endpoints; this App Service access restrictions choice leaves the App Service private endpoints explanation missing.
- **B — Correct.** An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
  An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution. For hardened and recoverable web application, App Service private endpoints supplies the service rule needed to give the application an inbound private address without making integration bidirectional.
- **C — Incorrect.** An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
  An App Service managed certificate can cover eligible custom domains but has feature and validation limitations. In the hardened and recoverable web application, this statement describes App Service managed certificates. Selecting App Service managed certificates for hardened and recoverable web application leaves App Service private endpoints unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a App Service private endpoints basis to give the application an inbound private address without making integration bidirectional.
- **D — Incorrect.** App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
  App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data. In the hardened and recoverable web application, this statement describes App Service backup storage. App Service private endpoints governs hardened and recoverable web application; App Service backup storage cannot support App Service private endpoints when operators must give the application an inbound private address without making integration bidirectional.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Use private endpoints for App Service](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint)

**Source reviewed:** 2026-08-31

## LAB16-Q10 — D

**Question:** The web hardening architecture note requires the hardened and recoverable web application environment to allow inbound requests only from approved network sources. Which statement defines the relevant web hardening boundary?

- **A — Incorrect.** The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
  The App Service minimum TLS setting rejects client handshakes below the configured protocol version. In the hardened and recoverable web application, this statement describes minimum inbound TLS. The minimum inbound TLS statement accurately describes minimum inbound TLS; however, hardened and recoverable web application needs App Service access restrictions to allow inbound requests only from approved network sources; minimum inbound TLS cannot replace App Service access restrictions.
- **B — Incorrect.** A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
  A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records. In the hardened and recoverable web application, this statement describes custom-domain DNS records. Selecting custom-domain DNS records for hardened and recoverable web application leaves App Service access restrictions unanswered in hardened and recoverable web application; the hardened and recoverable web application lacks a App Service access restrictions basis to allow inbound requests only from approved network sources.
- **C — Incorrect.** The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
  The backup schedule controls frequency and retention, subject to App Service tier and platform limits. In the hardened and recoverable web application, this statement describes backup schedules and retention. App Service access restrictions governs hardened and recoverable web application; backup schedules and retention cannot support App Service access restrictions when operators must allow inbound requests only from approved network sources.
- **D — Correct.** Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
  Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app. In the hardened and recoverable web application, this App Service access restrictions rule supports the need to allow inbound requests only from approved network sources.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Set up App Service access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions)

**Source reviewed:** 2026-08-31

## LAB16-Q11 — A

**Question:** Operators must automate the hardened and recoverable web application change needed to reject inbound clients that negotiate a protocol below the approved TLS version. Which web hardening operation belongs in the runbook?

- **A — Correct.** Set minTlsVersion to the approved baseline and confirm application clients support it.
  For the hardened and recoverable web application, the required minimum inbound TLS action is: set minTlsVersion to the approved baseline and confirm application clients support it. It makes the environment able to reject inbound clients that negotiate a protocol below the approved TLS version.
- **B — Incorrect.** Validate domain ownership and request the managed certificate only for a supported hostname and plan.
  Validate domain ownership and request the managed certificate only for a supported hostname and plan. In the hardened and recoverable web application, this action changes App Service managed certificates. Hardened and recoverable web application requires minimum inbound TLS; changing App Service managed certificates leaves minimum inbound TLS absent in hardened and recoverable web application; hardened and recoverable web application cannot reject inbound clients that negotiate a protocol below the approved TLS version.
- **C — Incorrect.** Create a private backup container and provide a short-lived SAS with the permissions required by backup.
  Create a private backup container and provide a short-lived SAS with the permissions required by backup. In the hardened and recoverable web application, this action changes App Service backup storage. App Service backup storage does not implement minimum inbound TLS for hardened and recoverable web application; the hardened and recoverable web application still cannot reject inbound clients that negotiate a protocol below the approved TLS version.
- **D — Incorrect.** Create the private endpoint, approve its connection, and link the correct private DNS zone.
  Create the private endpoint, approve its connection, and link the correct private DNS zone. In the hardened and recoverable web application, this action changes App Service private endpoints. Hardened and recoverable web application instead needs minimum inbound TLS: Set minTlsVersion to the approved baseline and confirm application clients support it. The App Service private endpoints action omits that minimum inbound TLS work.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q12 — B

**Question:** A hardened and recoverable web application review finds web hardening drift from the need to redirect unencrypted application requests to HTTPS. Which correction addresses that drift?

- **A — Incorrect.** Create the required DNS record type and preserve the ownership-verification record.
  Create the required DNS record type and preserve the ownership-verification record. In the hardened and recoverable web application, this action changes custom-domain DNS records. Hardened and recoverable web application requires HTTPS-only redirection; changing custom-domain DNS records leaves HTTPS-only redirection absent in hardened and recoverable web application; hardened and recoverable web application cannot redirect unencrypted application requests to HTTPS.
- **B — Correct.** Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
  Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. This changes HTTPS-only redirection in the hardened and recoverable web application, supplying the missing state needed to redirect unencrypted application requests to HTTPS.
- **C — Incorrect.** Configure a supported frequency, start time, and retention period that meets recovery requirements.
  Configure a supported frequency, start time, and retention period that meets recovery requirements. In the hardened and recoverable web application, this action changes backup schedules and retention. Hardened and recoverable web application instead needs HTTPS-only redirection: Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. The backup schedules and retention action omits that HTTPS-only redirection work.
- **D — Incorrect.** Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
  Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. In the hardened and recoverable web application, this action changes App Service access restrictions. Hardened and recoverable web application approved HTTPS-only redirection, not App Service access restrictions; only the HTTPS-only redirection change can redirect unencrypted application requests to HTTPS.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q13 — C

**Question:** The hardened and recoverable web application window permits only the web hardening change needed to bind a supported platform-managed certificate to a custom hostname. Which option respects the boundary?

- **A — Incorrect.** Publish the required asuid TXT record or supported validation record before adding the binding.
  Publish the required asuid TXT record or supported validation record before adding the binding. In the hardened and recoverable web application, this action changes domain ownership verification. Domain ownership verification does not implement App Service managed certificates for hardened and recoverable web application; the hardened and recoverable web application still cannot bind a supported platform-managed certificate to a custom hostname.
- **B — Incorrect.** Integrate the app with a dedicated delegated subnet for outbound private-resource access.
  Integrate the app with a dedicated delegated subnet for outbound private-resource access. In the hardened and recoverable web application, this action changes regional VNet integration. Hardened and recoverable web application instead needs App Service managed certificates: Validate domain ownership and request the managed certificate only for a supported hostname and plan. The regional VNet integration action omits that App Service managed certificates work.
- **C — Correct.** Validate domain ownership and request the managed certificate only for a supported hostname and plan.
  The hardened and recoverable web application must bind a supported platform-managed certificate to a custom hostname; this option performs its direct App Service managed certificates change: validate domain ownership and request the managed certificate only for a supported hostname and plan.
- **D — Incorrect.** Set minTlsVersion to the approved baseline and confirm application clients support it.
  Set minTlsVersion to the approved baseline and confirm application clients support it. In the hardened and recoverable web application, this action changes minimum inbound TLS. Hardened and recoverable web application requires App Service managed certificates; changing minimum inbound TLS leaves App Service managed certificates absent in hardened and recoverable web application; hardened and recoverable web application cannot bind a supported platform-managed certificate to a custom hostname.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q14 — B

**Question:** The web hardening preflight has passed; the hardened and recoverable web application must now publish the record type required for the chosen custom hostname. Which operation should run?

- **A — Incorrect.** Create a private backup container and provide a short-lived SAS with the permissions required by backup.
  Create a private backup container and provide a short-lived SAS with the permissions required by backup. In the hardened and recoverable web application, this action changes App Service backup storage. Hardened and recoverable web application instead needs custom-domain DNS records: Create the required DNS record type and preserve the ownership-verification record. The App Service backup storage action omits that custom-domain DNS records work.
- **B — Correct.** Create the required DNS record type and preserve the ownership-verification record.
  Create the required DNS record type and preserve the ownership-verification record. It is the least-change custom-domain DNS records path for the hardened and recoverable web application requirement to publish the record type required for the chosen custom hostname.
- **C — Incorrect.** Create the private endpoint, approve its connection, and link the correct private DNS zone.
  Create the private endpoint, approve its connection, and link the correct private DNS zone. In the hardened and recoverable web application, this action changes App Service private endpoints. Hardened and recoverable web application requires custom-domain DNS records; changing App Service private endpoints leaves custom-domain DNS records absent in hardened and recoverable web application; hardened and recoverable web application cannot publish the record type required for the chosen custom hostname.
- **D — Incorrect.** Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
  Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. In the hardened and recoverable web application, this action changes HTTPS-only redirection. HTTPS-only redirection does not implement custom-domain DNS records for hardened and recoverable web application; the hardened and recoverable web application still cannot publish the record type required for the chosen custom hostname.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q15 — B

**Question:** The hardened and recoverable web application plan must prove control of a hostname before binding it to the application while limiting the mutation scope to web hardening. Which action is appropriate?

- **A — Incorrect.** Configure a supported frequency, start time, and retention period that meets recovery requirements.
  Configure a supported frequency, start time, and retention period that meets recovery requirements. In the hardened and recoverable web application, this action changes backup schedules and retention. Hardened and recoverable web application approved domain ownership verification, not backup schedules and retention; only the domain ownership verification change can prove control of a hostname before binding it to the application.
- **B — Correct.** Publish the required asuid TXT record or supported validation record before adding the binding.
  Publish the required asuid TXT record or supported validation record before adding the binding. In hardened and recoverable web application, applying domain ownership verification is the scoped way to prove control of a hostname before binding it to the application.
- **C — Incorrect.** Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
  Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. In the hardened and recoverable web application, this action changes App Service access restrictions. App Service access restrictions does not implement domain ownership verification for hardened and recoverable web application; the hardened and recoverable web application still cannot prove control of a hostname before binding it to the application.
- **D — Incorrect.** Validate domain ownership and request the managed certificate only for a supported hostname and plan.
  Validate domain ownership and request the managed certificate only for a supported hostname and plan. In the hardened and recoverable web application, this action changes App Service managed certificates. Hardened and recoverable web application instead needs domain ownership verification: Publish the required asuid TXT record or supported validation record before adding the binding. The App Service managed certificates action omits that domain ownership verification work.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q16 — D

**Question:** A web hardening ticket in the hardened and recoverable web application says to write application backups to an authorized storage destination. Which web hardening action completes the hardened and recoverable web application request with minimal change?

- **A — Incorrect.** Integrate the app with a dedicated delegated subnet for outbound private-resource access.
  Integrate the app with a dedicated delegated subnet for outbound private-resource access. In the hardened and recoverable web application, this action changes regional VNet integration. Hardened and recoverable web application requires App Service backup storage; changing regional VNet integration leaves App Service backup storage absent in hardened and recoverable web application; hardened and recoverable web application cannot write application backups to an authorized storage destination.
- **B — Incorrect.** Set minTlsVersion to the approved baseline and confirm application clients support it.
  Set minTlsVersion to the approved baseline and confirm application clients support it. In the hardened and recoverable web application, this action changes minimum inbound TLS. Minimum inbound TLS does not implement App Service backup storage for hardened and recoverable web application; the hardened and recoverable web application still cannot write application backups to an authorized storage destination.
- **C — Incorrect.** Create the required DNS record type and preserve the ownership-verification record.
  Create the required DNS record type and preserve the ownership-verification record. In the hardened and recoverable web application, this action changes custom-domain DNS records. Hardened and recoverable web application instead needs App Service backup storage: Create a private backup container and provide a short-lived SAS with the permissions required by backup. The custom-domain DNS records action omits that App Service backup storage work.
- **D — Correct.** Create a private backup container and provide a short-lived SAS with the permissions required by backup.
  Create a private backup container and provide a short-lived SAS with the permissions required by backup. The hardened and recoverable web application uses this App Service backup storage operation to write application backups to an authorized storage destination within the approved scope.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q17 — B

**Question:** The approach for the hardened and recoverable web application is approved, but the web hardening environment still cannot retain scheduled backups for the required recovery window. Which implementation step closes the gap?

- **A — Incorrect.** Create the private endpoint, approve its connection, and link the correct private DNS zone.
  Create the private endpoint, approve its connection, and link the correct private DNS zone. In the hardened and recoverable web application, this action changes App Service private endpoints. App Service private endpoints does not implement backup schedules and retention for hardened and recoverable web application; the hardened and recoverable web application still cannot retain scheduled backups for the required recovery window.
- **B — Correct.** Configure a supported frequency, start time, and retention period that meets recovery requirements.
  For the hardened and recoverable web application, the required backup schedules and retention action is: configure a supported frequency, start time, and retention period that meets recovery requirements. It makes the environment able to retain scheduled backups for the required recovery window.
- **C — Incorrect.** Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
  Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. In the hardened and recoverable web application, this action changes HTTPS-only redirection. Hardened and recoverable web application approved backup schedules and retention, not HTTPS-only redirection; only the backup schedules and retention change can retain scheduled backups for the required recovery window.
- **D — Incorrect.** Publish the required asuid TXT record or supported validation record before adding the binding.
  Publish the required asuid TXT record or supported validation record before adding the binding. In the hardened and recoverable web application, this action changes domain ownership verification. Hardened and recoverable web application requires backup schedules and retention; changing domain ownership verification leaves backup schedules and retention absent in hardened and recoverable web application; hardened and recoverable web application cannot retain scheduled backups for the required recovery window.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q18 — C

**Question:** The application-platform administrator hardening and protecting a web app may change the hardened and recoverable web application only to send outbound application traffic into an approved regional virtual network. Which web hardening action stays within that assignment?

- **A — Incorrect.** Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
  Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. In the hardened and recoverable web application, this action changes App Service access restrictions. Hardened and recoverable web application instead needs regional VNet integration: Integrate the app with a dedicated delegated subnet for outbound private-resource access. The App Service access restrictions action omits that regional VNet integration work.
- **B — Incorrect.** Validate domain ownership and request the managed certificate only for a supported hostname and plan.
  Validate domain ownership and request the managed certificate only for a supported hostname and plan. In the hardened and recoverable web application, this action changes App Service managed certificates. Hardened and recoverable web application approved regional VNet integration, not App Service managed certificates; only the regional VNet integration change can send outbound application traffic into an approved regional virtual network.
- **C — Correct.** Integrate the app with a dedicated delegated subnet for outbound private-resource access.
  Integrate the app with a dedicated delegated subnet for outbound private-resource access. This changes regional VNet integration in the hardened and recoverable web application, supplying the missing state needed to send outbound application traffic into an approved regional virtual network.
- **D — Incorrect.** Create a private backup container and provide a short-lived SAS with the permissions required by backup.
  Create a private backup container and provide a short-lived SAS with the permissions required by backup. In the hardened and recoverable web application, this action changes App Service backup storage. App Service backup storage does not implement regional VNet integration for hardened and recoverable web application; the hardened and recoverable web application still cannot send outbound application traffic into an approved regional virtual network.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Integrate an App Service app with an Azure virtual network](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Source reviewed:** 2026-08-31

## LAB16-Q19 — C

**Question:** A web hardening dry run shows no hardened and recoverable web application command will give the application an inbound private address without making integration bidirectional. Which action belongs before execution?

- **A — Incorrect.** Set minTlsVersion to the approved baseline and confirm application clients support it.
  Set minTlsVersion to the approved baseline and confirm application clients support it. In the hardened and recoverable web application, this action changes minimum inbound TLS. Hardened and recoverable web application approved App Service private endpoints, not minimum inbound TLS; only the App Service private endpoints change can give the application an inbound private address without making integration bidirectional.
- **B — Incorrect.** Create the required DNS record type and preserve the ownership-verification record.
  Create the required DNS record type and preserve the ownership-verification record. In the hardened and recoverable web application, this action changes custom-domain DNS records. Hardened and recoverable web application requires App Service private endpoints; changing custom-domain DNS records leaves App Service private endpoints absent in hardened and recoverable web application; hardened and recoverable web application cannot give the application an inbound private address without making integration bidirectional.
- **C — Correct.** Create the private endpoint, approve its connection, and link the correct private DNS zone.
  The hardened and recoverable web application must give the application an inbound private address without making integration bidirectional; this option performs its direct App Service private endpoints change: create the private endpoint, approve its connection, and link the correct private DNS zone.
- **D — Incorrect.** Configure a supported frequency, start time, and retention period that meets recovery requirements.
  Configure a supported frequency, start time, and retention period that meets recovery requirements. In the hardened and recoverable web application, this action changes backup schedules and retention. Hardened and recoverable web application instead needs App Service private endpoints: Create the private endpoint, approve its connection, and link the correct private DNS zone. The backup schedules and retention action omits that App Service private endpoints work.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Use private endpoints for App Service](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint)

**Source reviewed:** 2026-08-31

## LAB16-Q20 — D

**Question:** For the hardened and recoverable web application, operators need to allow inbound requests only from approved network sources. Which change realizes that requirement?

- **A — Incorrect.** Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
  Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. In the hardened and recoverable web application, this action changes HTTPS-only redirection. Hardened and recoverable web application requires App Service access restrictions; changing HTTPS-only redirection leaves App Service access restrictions absent in hardened and recoverable web application; hardened and recoverable web application cannot allow inbound requests only from approved network sources.
- **B — Incorrect.** Publish the required asuid TXT record or supported validation record before adding the binding.
  Publish the required asuid TXT record or supported validation record before adding the binding. In the hardened and recoverable web application, this action changes domain ownership verification. Domain ownership verification does not implement App Service access restrictions for hardened and recoverable web application; the hardened and recoverable web application still cannot allow inbound requests only from approved network sources.
- **C — Incorrect.** Integrate the app with a dedicated delegated subnet for outbound private-resource access.
  Integrate the app with a dedicated delegated subnet for outbound private-resource access. In the hardened and recoverable web application, this action changes regional VNet integration. Hardened and recoverable web application instead needs App Service access restrictions: Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. The regional VNet integration action omits that App Service access restrictions work.
- **D — Correct.** Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
  Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. It is the least-change App Service access restrictions path for the hardened and recoverable web application requirement to allow inbound requests only from approved network sources.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Set up App Service access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions)

**Source reviewed:** 2026-08-31

## LAB16-Q21 — C

**Question:** The hardened and recoverable web application configuration is complete; the web hardening reviewers need evidence it can reject inbound clients that negotiate a protocol below the approved TLS version. Which observation shows success?

- **A — Incorrect.** Resolve the public record and query custom hostnames on the app.
  Resolve the public record and query custom hostnames on the app. In the hardened and recoverable web application, this check observes custom-domain DNS records. Hardened and recoverable web application output covers custom-domain DNS records, not minimum inbound TLS; the minimum inbound TLS requirement to reject inbound clients that negotiate a protocol below the approved TLS version remains unverified.
- **B — Incorrect.** Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. In the hardened and recoverable web application, this check observes backup schedules and retention. Backup schedules and retention success in hardened and recoverable web application cannot verify minimum inbound TLS; hardened and recoverable web application cannot reject inbound clients that negotiate a protocol below the approved TLS version until minimum inbound TLS evidence exists.
- **C — Correct.** Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. For hardened and recoverable web application, this minimum inbound TLS read confirms the service can reject inbound clients that negotiate a protocol below the approved TLS version.
- **D — Incorrect.** Query rule priorities, actions, source ranges, service tags, and unmatched action.
  Query rule priorities, actions, source ranges, service tags, and unmatched action. In the hardened and recoverable web application, this check observes App Service access restrictions. Hardened and recoverable web application could pass App Service access restrictions while minimum inbound TLS is wrong; hardened and recoverable web application still lacks minimum inbound TLS proof.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q22 — C

**Question:** The web hardening validation asks whether the hardened and recoverable web application can redirect unencrypted application requests to HTTPS. Which observable state is strongest?

- **A — Incorrect.** Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. In the hardened and recoverable web application, this check observes domain ownership verification. Domain ownership verification success in hardened and recoverable web application cannot verify HTTPS-only redirection; hardened and recoverable web application cannot redirect unencrypted application requests to HTTPS until HTTPS-only redirection evidence exists.
- **B — Incorrect.** Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. In the hardened and recoverable web application, this check observes regional VNet integration. Hardened and recoverable web application reads regional VNet integration, leaving HTTPS-only redirection unproved in hardened and recoverable web application; hardened and recoverable web application still has no HTTPS-only redirection proof.
- **C — Correct.** Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  Query httpsOnly and inspect hostNameSslStates for the custom hostname. The hardened and recoverable web application reads HTTPS-only redirection directly; that HTTPS-only redirection result proves the hardened and recoverable web application can redirect unencrypted application requests to HTTPS without another mutation.
- **D — Incorrect.** Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. In the hardened and recoverable web application, this check observes minimum inbound TLS. Hardened and recoverable web application output covers minimum inbound TLS, not HTTPS-only redirection; the HTTPS-only redirection requirement to redirect unencrypted application requests to HTTPS remains unverified.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q23 — C

**Question:** A hardened and recoverable web application review must prove the web hardening ability to bind a supported platform-managed certificate to a custom hostname. Which check avoids an adjacent feature?

- **A — Incorrect.** Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  Query backup configuration, storage URL redaction, enabled state, and the latest backup status. In the hardened and recoverable web application, this check observes App Service backup storage. Hardened and recoverable web application reads App Service backup storage, leaving App Service managed certificates unproved in hardened and recoverable web application; hardened and recoverable web application still has no App Service managed certificates proof.
- **B — Incorrect.** Resolve the app hostname privately and query the endpoint connection state and NIC address.
  Resolve the app hostname privately and query the endpoint connection state and NIC address. In the hardened and recoverable web application, this check observes App Service private endpoints. Hardened and recoverable web application could pass App Service private endpoints while App Service managed certificates is wrong; hardened and recoverable web application still lacks App Service managed certificates proof.
- **C — Correct.** Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  For the hardened and recoverable web application, this App Service managed certificates observation is decisive: query certificate expiration, thumbprint, hostname, and the app's SNI binding. It is hardened and recoverable web application evidence that operators can bind a supported platform-managed certificate to a custom hostname.
- **D — Incorrect.** Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  Query httpsOnly and inspect hostNameSslStates for the custom hostname. In the hardened and recoverable web application, this check observes HTTPS-only redirection. HTTPS-only redirection success in hardened and recoverable web application cannot verify App Service managed certificates; hardened and recoverable web application cannot bind a supported platform-managed certificate to a custom hostname until App Service managed certificates evidence exists.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q24 — B

**Question:** The hardened and recoverable web application evidence bundle needs a web hardening result showing it can publish the record type required for the chosen custom hostname. Which result belongs in the checkpoint?

- **A — Incorrect.** Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. In the hardened and recoverable web application, this check observes backup schedules and retention. Hardened and recoverable web application could pass backup schedules and retention while custom-domain DNS records is wrong; hardened and recoverable web application still lacks custom-domain DNS records proof.
- **B — Correct.** Resolve the public record and query custom hostnames on the app.
  Resolve the public record and query custom hostnames on the app. Because the hardened and recoverable web application check observes custom-domain DNS records, it independently verifies the requirement to publish the record type required for the chosen custom hostname.
- **C — Incorrect.** Query rule priorities, actions, source ranges, service tags, and unmatched action.
  Query rule priorities, actions, source ranges, service tags, and unmatched action. In the hardened and recoverable web application, this check observes App Service access restrictions. App Service access restrictions success in hardened and recoverable web application cannot verify custom-domain DNS records; hardened and recoverable web application cannot publish the record type required for the chosen custom hostname until custom-domain DNS records evidence exists.
- **D — Incorrect.** Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  Query certificate expiration, thumbprint, hostname, and the app's SNI binding. In the hardened and recoverable web application, this check observes App Service managed certificates. Hardened and recoverable web application reads App Service managed certificates, leaving custom-domain DNS records unproved in hardened and recoverable web application; hardened and recoverable web application still has no custom-domain DNS records proof.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q25 — A

**Question:** Before hardened and recoverable web application cleanup, the web hardening team must reconfirm it can prove control of a hostname before binding it to the application. Which read-only inspection should run?

- **A — Correct.** Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  The hardened and recoverable web application validator needs this domain ownership verification result: resolve the TXT record and confirm its value matches the app's customDomainVerificationId. It proves the outcome to prove control of a hostname before binding it to the application rather than an adjacent checkpoint.
- **B — Incorrect.** Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. In the hardened and recoverable web application, this check observes regional VNet integration. Regional VNet integration success in hardened and recoverable web application cannot verify domain ownership verification; hardened and recoverable web application cannot prove control of a hostname before binding it to the application until domain ownership verification evidence exists.
- **C — Incorrect.** Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. In the hardened and recoverable web application, this check observes minimum inbound TLS. Hardened and recoverable web application reads minimum inbound TLS, leaving domain ownership verification unproved in hardened and recoverable web application; hardened and recoverable web application still has no domain ownership verification proof.
- **D — Incorrect.** Resolve the public record and query custom hostnames on the app.
  Resolve the public record and query custom hostnames on the app. In the hardened and recoverable web application, this check observes custom-domain DNS records. Hardened and recoverable web application could pass custom-domain DNS records while domain ownership verification is wrong; hardened and recoverable web application still lacks domain ownership verification proof.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q26 — A

**Question:** The hardened and recoverable web application setup reports success after the web hardening attempt to write application backups to an authorized storage destination. Which web hardening read-only observation proves the hardened and recoverable web application outcome?

- **A — Correct.** Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  Query backup configuration, storage URL redaction, enabled state, and the latest backup status. This is independent App Service backup storage evidence for the hardened and recoverable web application, even if hardened and recoverable web application setup reports success before App Service backup storage becomes observable.
- **B — Incorrect.** Resolve the app hostname privately and query the endpoint connection state and NIC address.
  Resolve the app hostname privately and query the endpoint connection state and NIC address. In the hardened and recoverable web application, this check observes App Service private endpoints. Hardened and recoverable web application reads App Service private endpoints, leaving App Service backup storage unproved in hardened and recoverable web application; hardened and recoverable web application still has no App Service backup storage proof.
- **C — Incorrect.** Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  Query httpsOnly and inspect hostNameSslStates for the custom hostname. In the hardened and recoverable web application, this check observes HTTPS-only redirection. Hardened and recoverable web application could pass HTTPS-only redirection while App Service backup storage is wrong; hardened and recoverable web application still lacks App Service backup storage proof.
- **D — Incorrect.** Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. In the hardened and recoverable web application, this check observes domain ownership verification. Hardened and recoverable web application output covers domain ownership verification, not App Service backup storage; the App Service backup storage requirement to write application backups to an authorized storage destination remains unverified.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q27 — A

**Question:** The web hardening log says the hardened and recoverable web application can now retain scheduled backups for the required recovery window. Which web hardening state should the hardened and recoverable web application acceptance test retain?

- **A — Correct.** Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. For hardened and recoverable web application, this backup schedules and retention read confirms the service can retain scheduled backups for the required recovery window.
- **B — Incorrect.** Query rule priorities, actions, source ranges, service tags, and unmatched action.
  Query rule priorities, actions, source ranges, service tags, and unmatched action. In the hardened and recoverable web application, this check observes App Service access restrictions. Hardened and recoverable web application could pass App Service access restrictions while backup schedules and retention is wrong; hardened and recoverable web application still lacks backup schedules and retention proof.
- **C — Incorrect.** Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  Query certificate expiration, thumbprint, hostname, and the app's SNI binding. In the hardened and recoverable web application, this check observes App Service managed certificates. Hardened and recoverable web application output covers App Service managed certificates, not backup schedules and retention; the backup schedules and retention requirement to retain scheduled backups for the required recovery window remains unverified.
- **D — Incorrect.** Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  Query backup configuration, storage URL redaction, enabled state, and the latest backup status. In the hardened and recoverable web application, this check observes App Service backup storage. App Service backup storage success in hardened and recoverable web application cannot verify backup schedules and retention; hardened and recoverable web application cannot retain scheduled backups for the required recovery window until backup schedules and retention evidence exists.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q28 — B

**Question:** The hardened and recoverable web application rejects web hardening exit status as proof it can send outbound application traffic into an approved regional virtual network. Which hardened and recoverable web application result is valid evidence?

- **A — Incorrect.** Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. In the hardened and recoverable web application, this check observes minimum inbound TLS. Hardened and recoverable web application could pass minimum inbound TLS while regional VNet integration is wrong; hardened and recoverable web application still lacks regional VNet integration proof.
- **B — Correct.** Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. The hardened and recoverable web application reads regional VNet integration directly; that regional VNet integration result proves the hardened and recoverable web application can send outbound application traffic into an approved regional virtual network without another mutation.
- **C — Incorrect.** Resolve the public record and query custom hostnames on the app.
  Resolve the public record and query custom hostnames on the app. In the hardened and recoverable web application, this check observes custom-domain DNS records. Custom-domain DNS records success in hardened and recoverable web application cannot verify regional VNet integration; hardened and recoverable web application cannot send outbound application traffic into an approved regional virtual network until regional VNet integration evidence exists.
- **D — Incorrect.** Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. In the hardened and recoverable web application, this check observes backup schedules and retention. Hardened and recoverable web application reads backup schedules and retention, leaving regional VNet integration unproved in hardened and recoverable web application; hardened and recoverable web application still has no regional VNet integration proof.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Integrate an App Service app with an Azure virtual network](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Source reviewed:** 2026-08-31

## LAB16-Q29 — C

**Question:** The web hardening validator needs one hardened and recoverable web application query after the change to give the application an inbound private address without making integration bidirectional. Which web hardening property should the hardened and recoverable web application validator inspect?

- **A — Incorrect.** Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  Query httpsOnly and inspect hostNameSslStates for the custom hostname. In the hardened and recoverable web application, this check observes HTTPS-only redirection. Hardened and recoverable web application output covers HTTPS-only redirection, not App Service private endpoints; the App Service private endpoints requirement to give the application an inbound private address without making integration bidirectional remains unverified.
- **B — Incorrect.** Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. In the hardened and recoverable web application, this check observes domain ownership verification. Domain ownership verification success in hardened and recoverable web application cannot verify App Service private endpoints; hardened and recoverable web application cannot give the application an inbound private address without making integration bidirectional until App Service private endpoints evidence exists.
- **C — Correct.** Resolve the app hostname privately and query the endpoint connection state and NIC address.
  For the hardened and recoverable web application, this App Service private endpoints observation is decisive: resolve the app hostname privately and query the endpoint connection state and NIC address. It is hardened and recoverable web application evidence that operators can give the application an inbound private address without making integration bidirectional.
- **D — Incorrect.** Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. In the hardened and recoverable web application, this check observes regional VNet integration. Hardened and recoverable web application could pass regional VNet integration while App Service private endpoints is wrong; hardened and recoverable web application still lacks App Service private endpoints proof.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Use private endpoints for App Service](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint)

**Source reviewed:** 2026-08-31

## LAB16-Q30 — A

**Question:** The application-platform administrator hardening and protecting a web app must confirm the hardened and recoverable web application, without mutation, can allow inbound requests only from approved network sources. Which web hardening check qualifies?

- **A — Correct.** Query rule priorities, actions, source ranges, service tags, and unmatched action.
  Query rule priorities, actions, source ranges, service tags, and unmatched action. Because the hardened and recoverable web application check observes App Service access restrictions, it independently verifies the requirement to allow inbound requests only from approved network sources.
- **B — Incorrect.** Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  Query certificate expiration, thumbprint, hostname, and the app's SNI binding. In the hardened and recoverable web application, this check observes App Service managed certificates. Hardened and recoverable web application reads App Service managed certificates, leaving App Service access restrictions unproved in hardened and recoverable web application; hardened and recoverable web application still has no App Service access restrictions proof.
- **C — Incorrect.** Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  Query backup configuration, storage URL redaction, enabled state, and the latest backup status. In the hardened and recoverable web application, this check observes App Service backup storage. Hardened and recoverable web application could pass App Service backup storage while App Service access restrictions is wrong; hardened and recoverable web application still lacks App Service access restrictions proof.
- **D — Incorrect.** Resolve the app hostname privately and query the endpoint connection state and NIC address.
  Resolve the app hostname privately and query the endpoint connection state and NIC address. In the hardened and recoverable web application, this check observes App Service private endpoints. Hardened and recoverable web application output covers App Service private endpoints, not App Service access restrictions; the App Service access restrictions requirement to allow inbound requests only from approved network sources remains unverified.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Set up App Service access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions)

**Source reviewed:** 2026-08-31

## LAB16-Q31 — D

**Question:** The web hardening evidence shows the hardened and recoverable web application cannot reject inbound clients that negotiate a protocol below the approved TLS version. Which root cause fits that evidence?

- **A — Incorrect.** HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
  HTTPS Only is enabled, but the custom hostname has no valid certificate binding. The hardened and recoverable web application fault concerns HTTPS-only redirection. Hardened and recoverable web application has HTTPS-only redirection impact, but minimum inbound TLS is the hardened and recoverable web application failed path; the HTTPS-only redirection state cannot produce minimum inbound TLS failure.
- **B — Incorrect.** The SAS expired before the scheduled backup attempted to write its archive.
  The SAS expired before the scheduled backup attempted to write its archive. The hardened and recoverable web application fault concerns App Service backup storage. Hardened and recoverable web application could repair App Service backup storage while minimum inbound TLS stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to reject inbound clients that negotiate a protocol below the approved TLS version.
- **C — Incorrect.** A broad deny rule has a higher priority than the required allow rule.
  A broad deny rule has a higher priority than the required allow rule. The hardened and recoverable web application fault concerns App Service access restrictions. Hardened and recoverable web application failed on minimum inbound TLS; this App Service access restrictions finding redirects hardened and recoverable web application remediation away from minimum inbound TLS.
- **D — Correct.** A legacy client negotiates only a TLS version below the app's minimum.
  The hardened and recoverable web application cannot reject inbound clients that negotiate a protocol below the approved TLS version because of this minimum inbound TLS defect: a legacy client negotiates only a TLS version below the app's minimum. The symptom and repair align.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q32 — B

**Question:** Although the hardened and recoverable web application is meant to let the web hardening redirect unencrypted application requests to HTTPS, its checkpoint fails. Which web hardening defect explains the failure?

- **A — Incorrect.** The requested hostname or DNS configuration is not eligible for a managed certificate.
  The requested hostname or DNS configuration is not eligible for a managed certificate. The hardened and recoverable web application fault concerns App Service managed certificates. Hardened and recoverable web application could repair App Service managed certificates while HTTPS-only redirection stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to redirect unencrypted application requests to HTTPS.
- **B — Correct.** HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
  HTTPS Only is enabled, but the custom hostname has no valid certificate binding. Removing this HTTPS-only redirection condition lets the hardened and recoverable web application redirect unencrypted application requests to HTTPS while leaving healthy controls unchanged.
- **C — Incorrect.** The selected plan tier does not support the required automated backup feature.
  The selected plan tier does not support the required automated backup feature. The hardened and recoverable web application fault concerns backup schedules and retention. Hardened and recoverable web application may fix backup schedules and retention, yet HTTPS-only redirection still fails; this hardened and recoverable web application diagnosis of backup schedules and retention is wrong for HTTPS-only redirection.
- **D — Incorrect.** A legacy client negotiates only a TLS version below the app's minimum.
  A legacy client negotiates only a TLS version below the app's minimum. The hardened and recoverable web application fault concerns minimum inbound TLS. Hardened and recoverable web application has minimum inbound TLS impact, but HTTPS-only redirection is the hardened and recoverable web application failed path; the minimum inbound TLS state cannot produce HTTPS-only redirection failure.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q33 — B

**Question:** The web hardening support team isolated the hardened and recoverable web application incident to the attempt to bind a supported platform-managed certificate to a custom hostname. Which condition prevents success?

- **A — Incorrect.** The CNAME points to a deployment-slot hostname that is not the approved production target.
  The CNAME points to a deployment-slot hostname that is not the approved production target. The hardened and recoverable web application fault concerns custom-domain DNS records. Hardened and recoverable web application failed on App Service managed certificates; this custom-domain DNS records finding redirects hardened and recoverable web application remediation away from App Service managed certificates.
- **B — Correct.** The requested hostname or DNS configuration is not eligible for a managed certificate.
  The requested hostname or DNS configuration is not eligible for a managed certificate. In hardened and recoverable web application, this App Service managed certificates cause matches the failure to bind a supported platform-managed certificate to a custom hostname.
- **C — Incorrect.** The design expects VNet integration alone to remove the public inbound endpoint.
  The design expects VNet integration alone to remove the public inbound endpoint. The hardened and recoverable web application fault concerns regional VNet integration. Hardened and recoverable web application has regional VNet integration impact, but App Service managed certificates is the hardened and recoverable web application failed path; the regional VNet integration state cannot produce App Service managed certificates failure.
- **D — Incorrect.** HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
  HTTPS Only is enabled, but the custom hostname has no valid certificate binding. The hardened and recoverable web application fault concerns HTTPS-only redirection. Hardened and recoverable web application could repair HTTPS-only redirection while App Service managed certificates stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to bind a supported platform-managed certificate to a custom hostname.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q34 — A

**Question:** A hardened and recoverable web application query surprises the application-platform administrator hardening and protecting a web app during the web hardening attempt to publish the record type required for the chosen custom hostname. Which finding explains it?

- **A — Correct.** The CNAME points to a deployment-slot hostname that is not the approved production target.
  The CNAME points to a deployment-slot hostname that is not the approved production target. This hardened and recoverable web application condition breaks custom-domain DNS records, explaining why operators cannot publish the record type required for the chosen custom hostname.
- **B — Incorrect.** The TXT record was created under the wrong DNS label.
  The TXT record was created under the wrong DNS label. The hardened and recoverable web application fault concerns domain ownership verification. Hardened and recoverable web application has domain ownership verification impact, but custom-domain DNS records is the hardened and recoverable web application failed path; the domain ownership verification state cannot produce custom-domain DNS records failure.
- **C — Incorrect.** DNS still resolves the app hostname to its public endpoint from inside the virtual network.
  DNS still resolves the app hostname to its public endpoint from inside the virtual network. The hardened and recoverable web application fault concerns App Service private endpoints. Hardened and recoverable web application could repair App Service private endpoints while custom-domain DNS records stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to publish the record type required for the chosen custom hostname.
- **D — Incorrect.** The requested hostname or DNS configuration is not eligible for a managed certificate.
  The requested hostname or DNS configuration is not eligible for a managed certificate. The hardened and recoverable web application fault concerns App Service managed certificates. Hardened and recoverable web application failed on custom-domain DNS records; this App Service managed certificates finding redirects hardened and recoverable web application remediation away from custom-domain DNS records.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q35 — D

**Question:** Other hardened and recoverable web application components are healthy, but the web hardening still cannot prove control of a hostname before binding it to the application. Which state causes the isolated failure?

- **A — Incorrect.** The SAS expired before the scheduled backup attempted to write its archive.
  The SAS expired before the scheduled backup attempted to write its archive. The hardened and recoverable web application fault concerns App Service backup storage. Hardened and recoverable web application has App Service backup storage impact, but domain ownership verification is the hardened and recoverable web application failed path; the App Service backup storage state cannot produce domain ownership verification failure.
- **B — Incorrect.** A broad deny rule has a higher priority than the required allow rule.
  A broad deny rule has a higher priority than the required allow rule. The hardened and recoverable web application fault concerns App Service access restrictions. Hardened and recoverable web application could repair App Service access restrictions while domain ownership verification stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to prove control of a hostname before binding it to the application.
- **C — Incorrect.** The CNAME points to a deployment-slot hostname that is not the approved production target.
  The CNAME points to a deployment-slot hostname that is not the approved production target. The hardened and recoverable web application fault concerns custom-domain DNS records. Hardened and recoverable web application failed on domain ownership verification; this custom-domain DNS records finding redirects hardened and recoverable web application remediation away from domain ownership verification.
- **D — Correct.** The TXT record was created under the wrong DNS label.
  For the hardened and recoverable web application, the domain ownership verification failure is causal: the TXT record was created under the wrong DNS label. Correcting it restores the ability to prove control of a hostname before binding it to the application.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q36 — D

**Question:** During a web hardening fault drill, the hardened and recoverable web application does not write application backups to an authorized storage destination. Which finding identifies the defect?

- **A — Incorrect.** The selected plan tier does not support the required automated backup feature.
  The selected plan tier does not support the required automated backup feature. The hardened and recoverable web application fault concerns backup schedules and retention. Hardened and recoverable web application could repair backup schedules and retention while App Service backup storage stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to write application backups to an authorized storage destination.
- **B — Incorrect.** A legacy client negotiates only a TLS version below the app's minimum.
  A legacy client negotiates only a TLS version below the app's minimum. The hardened and recoverable web application fault concerns minimum inbound TLS. Hardened and recoverable web application failed on App Service backup storage; this minimum inbound TLS finding redirects hardened and recoverable web application remediation away from App Service backup storage.
- **C — Incorrect.** The TXT record was created under the wrong DNS label.
  The TXT record was created under the wrong DNS label. The hardened and recoverable web application fault concerns domain ownership verification. Hardened and recoverable web application may fix domain ownership verification, yet App Service backup storage still fails; this hardened and recoverable web application diagnosis of domain ownership verification is wrong for App Service backup storage.
- **D — Correct.** The SAS expired before the scheduled backup attempted to write its archive.
  The SAS expired before the scheduled backup attempted to write its archive. The finding is specific to App Service backup storage in the hardened and recoverable web application; repairing App Service backup storage restores the hardened and recoverable web application ability to write application backups to an authorized storage destination.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q37 — C

**Question:** The hardened and recoverable web application setup finishes, yet the web hardening cannot retain scheduled backups for the required recovery window. Which misconfiguration explains the mismatch?

- **A — Incorrect.** The design expects VNet integration alone to remove the public inbound endpoint.
  The design expects VNet integration alone to remove the public inbound endpoint. The hardened and recoverable web application fault concerns regional VNet integration. Hardened and recoverable web application failed on backup schedules and retention; this regional VNet integration finding redirects hardened and recoverable web application remediation away from backup schedules and retention.
- **B — Incorrect.** HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
  HTTPS Only is enabled, but the custom hostname has no valid certificate binding. The hardened and recoverable web application fault concerns HTTPS-only redirection. Hardened and recoverable web application may fix HTTPS-only redirection, yet backup schedules and retention still fails; this hardened and recoverable web application diagnosis of HTTPS-only redirection is wrong for backup schedules and retention.
- **C — Correct.** The selected plan tier does not support the required automated backup feature.
  The hardened and recoverable web application cannot retain scheduled backups for the required recovery window because of this backup schedules and retention defect: the selected plan tier does not support the required automated backup feature. The symptom and repair align.
- **D — Incorrect.** The SAS expired before the scheduled backup attempted to write its archive.
  The SAS expired before the scheduled backup attempted to write its archive. The hardened and recoverable web application fault concerns App Service backup storage. Hardened and recoverable web application could repair App Service backup storage while backup schedules and retention stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to retain scheduled backups for the required recovery window.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q38 — C

**Question:** A web hardening break/fix in the hardened and recoverable web application fails when operators try to send outbound application traffic into an approved regional virtual network. Which diagnosis fits?

- **A — Incorrect.** DNS still resolves the app hostname to its public endpoint from inside the virtual network.
  DNS still resolves the app hostname to its public endpoint from inside the virtual network. The hardened and recoverable web application fault concerns App Service private endpoints. Hardened and recoverable web application may fix App Service private endpoints, yet regional VNet integration still fails; this hardened and recoverable web application diagnosis of App Service private endpoints is wrong for regional VNet integration.
- **B — Incorrect.** The requested hostname or DNS configuration is not eligible for a managed certificate.
  The requested hostname or DNS configuration is not eligible for a managed certificate. The hardened and recoverable web application fault concerns App Service managed certificates. Hardened and recoverable web application has App Service managed certificates impact, but regional VNet integration is the hardened and recoverable web application failed path; the App Service managed certificates state cannot produce regional VNet integration failure.
- **C — Correct.** The design expects VNet integration alone to remove the public inbound endpoint.
  The design expects VNet integration alone to remove the public inbound endpoint. Removing this regional VNet integration condition lets the hardened and recoverable web application send outbound application traffic into an approved regional virtual network while leaving healthy controls unchanged.
- **D — Incorrect.** The selected plan tier does not support the required automated backup feature.
  The selected plan tier does not support the required automated backup feature. The hardened and recoverable web application fault concerns backup schedules and retention. Hardened and recoverable web application failed on regional VNet integration; this backup schedules and retention finding redirects hardened and recoverable web application remediation away from regional VNet integration.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Integrate an App Service app with an Azure virtual network](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Source reviewed:** 2026-08-31

## LAB16-Q39 — C

**Question:** The hardened and recoverable web application troubleshooting scope is the web hardening need to give the application an inbound private address without making integration bidirectional. Which condition should be corrected first?

- **A — Incorrect.** A broad deny rule has a higher priority than the required allow rule.
  A broad deny rule has a higher priority than the required allow rule. The hardened and recoverable web application fault concerns App Service access restrictions. Hardened and recoverable web application has App Service access restrictions impact, but App Service private endpoints is the hardened and recoverable web application failed path; the App Service access restrictions state cannot produce App Service private endpoints failure.
- **B — Incorrect.** The CNAME points to a deployment-slot hostname that is not the approved production target.
  The CNAME points to a deployment-slot hostname that is not the approved production target. The hardened and recoverable web application fault concerns custom-domain DNS records. Hardened and recoverable web application could repair custom-domain DNS records while App Service private endpoints stays broken in hardened and recoverable web application; the hardened and recoverable web application remains unable to give the application an inbound private address without making integration bidirectional.
- **C — Correct.** DNS still resolves the app hostname to its public endpoint from inside the virtual network.
  DNS still resolves the app hostname to its public endpoint from inside the virtual network. In hardened and recoverable web application, this App Service private endpoints cause matches the failure to give the application an inbound private address without making integration bidirectional.
- **D — Incorrect.** The design expects VNet integration alone to remove the public inbound endpoint.
  The design expects VNet integration alone to remove the public inbound endpoint. The hardened and recoverable web application fault concerns regional VNet integration. Hardened and recoverable web application may fix regional VNet integration, yet App Service private endpoints still fails; this hardened and recoverable web application diagnosis of regional VNet integration is wrong for App Service private endpoints.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Use private endpoints for App Service](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint)

**Source reviewed:** 2026-08-31

## LAB16-Q40 — A

**Question:** The hardened and recoverable web application result is partial because the web hardening cannot allow inbound requests only from approved network sources. Which condition accounts for that result?

- **A — Correct.** A broad deny rule has a higher priority than the required allow rule.
  A broad deny rule has a higher priority than the required allow rule. This hardened and recoverable web application condition breaks App Service access restrictions, explaining why operators cannot allow inbound requests only from approved network sources.
- **B — Incorrect.** A legacy client negotiates only a TLS version below the app's minimum.
  A legacy client negotiates only a TLS version below the app's minimum. The hardened and recoverable web application fault concerns minimum inbound TLS. Hardened and recoverable web application failed on App Service access restrictions; this minimum inbound TLS finding redirects hardened and recoverable web application remediation away from App Service access restrictions.
- **C — Incorrect.** The TXT record was created under the wrong DNS label.
  The TXT record was created under the wrong DNS label. The hardened and recoverable web application fault concerns domain ownership verification. Hardened and recoverable web application may fix domain ownership verification, yet App Service access restrictions still fails; this hardened and recoverable web application diagnosis of domain ownership verification is wrong for App Service access restrictions.
- **D — Incorrect.** DNS still resolves the app hostname to its public endpoint from inside the virtual network.
  DNS still resolves the app hostname to its public endpoint from inside the virtual network. The hardened and recoverable web application fault concerns App Service private endpoints. Hardened and recoverable web application has App Service private endpoints impact, but App Service access restrictions is the hardened and recoverable web application failed path; the App Service private endpoints state cannot produce App Service access restrictions failure.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Set up App Service access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions)

**Source reviewed:** 2026-08-31

## LAB16-Q41 — A

**Question:** At the hardened and recoverable web application approval gate, operators must show that the web hardening can reject inbound clients that negotiate a protocol below the approved TLS version. Which web hardening configure-and-check pair is defensible?

- **A — Correct.** First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  For the hardened and recoverable web application, the safe minimum inbound TLS order is: first, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. The hardened and recoverable web application records minimum inbound TLS proof after configuration.
- **B — Incorrect.** First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding. This hardened and recoverable web application pair serves App Service managed certificates. Hardened and recoverable web application proves App Service managed certificates, but minimum inbound TLS lacks implementation in hardened and recoverable web application and minimum inbound TLS proof; the minimum inbound TLS outcome to reject inbound clients that negotiate a protocol below the approved TLS version remains open.
- **C — Incorrect.** First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. This hardened and recoverable web application pair serves backup schedules and retention. Hardened and recoverable web application uses backup schedules and retention for both steps; minimum inbound TLS remains untouched in hardened and recoverable web application, so its minimum inbound TLS gate to reject inbound clients that negotiate a protocol below the approved TLS version fails.
- **D — Incorrect.** First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. This hardened and recoverable web application pair serves regional VNet integration. Hardened and recoverable web application closes regional VNet integration, not minimum inbound TLS; without the minimum inbound TLS workflow, it cannot reject inbound clients that negotiate a protocol below the approved TLS version.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q42 — C

**Question:** The hardened and recoverable web application forbids a partial web hardening result. Operators must first redirect unencrypted application requests to HTTPS and afterward confirm the hardened and recoverable web application outcome. Which web hardening sequence is complete?

- **A — Incorrect.** First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
  First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app. This hardened and recoverable web application pair serves custom-domain DNS records. Hardened and recoverable web application proves custom-domain DNS records, but HTTPS-only redirection lacks implementation in hardened and recoverable web application and HTTPS-only redirection proof; the HTTPS-only redirection outcome to redirect unencrypted application requests to HTTPS remains open.
- **B — Incorrect.** First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. This hardened and recoverable web application pair serves regional VNet integration. Hardened and recoverable web application uses regional VNet integration for both steps; HTTPS-only redirection remains untouched in hardened and recoverable web application, so its HTTPS-only redirection gate to redirect unencrypted application requests to HTTPS fails.
- **C — Correct.** First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname. The hardened and recoverable web application uses its HTTPS-only redirection mutation gate and HTTPS-only redirection verification gate before it can redirect unencrypted application requests to HTTPS.
- **D — Incorrect.** First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
  First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address. This hardened and recoverable web application pair serves App Service private endpoints. App Service private endpoints cannot replace HTTPS-only redirection in hardened and recoverable web application. Use this HTTPS-only redirection pair instead: First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q43 — A

**Question:** Only the hardened and recoverable web application change needed to bind a supported platform-managed certificate to a custom hostname is allowed, and web hardening proof is mandatory. Which pair fits?

- **A — Correct.** First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  The hardened and recoverable web application gets a complete App Service managed certificates sequence here: first, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding. Read-back evidence follows the change.
- **B — Incorrect.** First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. This hardened and recoverable web application pair serves domain ownership verification. Hardened and recoverable web application closes domain ownership verification, not App Service managed certificates; without the App Service managed certificates workflow, it cannot bind a supported platform-managed certificate to a custom hostname.
- **C — Incorrect.** First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
  First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address. This hardened and recoverable web application pair serves App Service private endpoints. App Service private endpoints cannot replace App Service managed certificates in hardened and recoverable web application. Use this App Service managed certificates pair instead: First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- **D — Incorrect.** First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
  First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action. This hardened and recoverable web application pair serves App Service access restrictions. Hardened and recoverable web application proves App Service access restrictions, but App Service managed certificates lacks implementation in hardened and recoverable web application and App Service managed certificates proof; the App Service managed certificates outcome to bind a supported platform-managed certificate to a custom hostname remains open.

**Objectives:** `CP-APP-04`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Secure an App Service custom DNS name with TLS](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings)

**Source reviewed:** 2026-08-31

## LAB16-Q44 — A

**Question:** The hardened and recoverable web application runbook separates web hardening mutation from validation while it must publish the record type required for the chosen custom hostname. Which sequence proves it cleanly?

- **A — Correct.** First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
  First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app. This ordered custom-domain DNS records workflow lets the hardened and recoverable web application publish the record type required for the chosen custom hostname and then verify the resulting state.
- **B — Incorrect.** First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status. This hardened and recoverable web application pair serves App Service backup storage. App Service backup storage cannot replace custom-domain DNS records in hardened and recoverable web application. Use this custom-domain DNS records pair instead: First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
- **C — Incorrect.** First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
  First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action. This hardened and recoverable web application pair serves App Service access restrictions. Hardened and recoverable web application proves App Service access restrictions, but custom-domain DNS records lacks implementation in hardened and recoverable web application and custom-domain DNS records proof; the custom-domain DNS records outcome to publish the record type required for the chosen custom hostname remains open.
- **D — Incorrect.** First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. This hardened and recoverable web application pair serves minimum inbound TLS. Hardened and recoverable web application uses minimum inbound TLS for both steps; custom-domain DNS records remains untouched in hardened and recoverable web application, so its custom-domain DNS records gate to publish the record type required for the chosen custom hostname fails.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q45 — D

**Question:** The hardened and recoverable web application checkpoint requires both this web hardening outcome—prove control of a hostname before binding it to the application—and a read-only hardened and recoverable web application state check. Which web hardening response is complete?

- **A — Incorrect.** First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. This hardened and recoverable web application pair serves backup schedules and retention. Backup schedules and retention cannot replace domain ownership verification in hardened and recoverable web application. Use this domain ownership verification pair instead: First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- **B — Incorrect.** First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. This hardened and recoverable web application pair serves minimum inbound TLS. Hardened and recoverable web application proves minimum inbound TLS, but domain ownership verification lacks implementation in hardened and recoverable web application and domain ownership verification proof; the domain ownership verification outcome to prove control of a hostname before binding it to the application remains open.
- **C — Incorrect.** First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname. This hardened and recoverable web application pair serves HTTPS-only redirection. Hardened and recoverable web application uses HTTPS-only redirection for both steps; domain ownership verification remains untouched in hardened and recoverable web application, so its domain ownership verification gate to prove control of a hostname before binding it to the application fails.
- **D — Correct.** First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. For hardened and recoverable web application, the domain ownership verification operation precedes its domain ownership verification read-back check, allowing it to prove control of a hostname before binding it to the application.

**Objectives:** `CP-APP-05`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Map a custom DNS name to App Service](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-domain)

**Source reviewed:** 2026-08-31

## LAB16-Q46 — B

**Question:** The hardened and recoverable web application runbook must write application backups to an authorized storage destination, then retain web hardening read-back evidence. Which hardened and recoverable web application pair completes both duties?

- **A — Incorrect.** First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. This hardened and recoverable web application pair serves regional VNet integration. Hardened and recoverable web application proves regional VNet integration, but App Service backup storage lacks implementation in hardened and recoverable web application and App Service backup storage proof; the App Service backup storage outcome to write application backups to an authorized storage destination remains open.
- **B — Correct.** First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status. In the hardened and recoverable web application, the first App Service backup storage step runs; the hardened and recoverable web application then reads App Service backup storage state to prove it can write application backups to an authorized storage destination.
- **C — Incorrect.** First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname. This hardened and recoverable web application pair serves HTTPS-only redirection. Hardened and recoverable web application closes HTTPS-only redirection, not App Service backup storage; without the App Service backup storage workflow, it cannot write application backups to an authorized storage destination.
- **D — Incorrect.** First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding. This hardened and recoverable web application pair serves App Service managed certificates. App Service managed certificates cannot replace App Service backup storage in hardened and recoverable web application. Use this App Service backup storage pair instead: First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-1) (`LAB16-CP01`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q47 — D

**Question:** To satisfy the web hardening requirement, operators must change the hardened and recoverable web application configuration and prove it can retain scheduled backups for the required recovery window. Which sequence is coherent?

- **A — Incorrect.** First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
  First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address. This hardened and recoverable web application pair serves App Service private endpoints. Hardened and recoverable web application uses App Service private endpoints for both steps; backup schedules and retention remains untouched in hardened and recoverable web application, so its backup schedules and retention gate to retain scheduled backups for the required recovery window fails.
- **B — Incorrect.** First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
  First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding. This hardened and recoverable web application pair serves App Service managed certificates. Hardened and recoverable web application closes App Service managed certificates, not backup schedules and retention; without the backup schedules and retention workflow, it cannot retain scheduled backups for the required recovery window.
- **C — Incorrect.** First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
  First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app. This hardened and recoverable web application pair serves custom-domain DNS records. Custom-domain DNS records cannot replace backup schedules and retention in hardened and recoverable web application. Use this backup schedules and retention pair instead: First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- **D — Correct.** First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  For the hardened and recoverable web application, the safe backup schedules and retention order is: first, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. The hardened and recoverable web application records backup schedules and retention proof after configuration.

**Objectives:** `CP-APP-06`

**Remediation:** [Repeat the mapped guided task](../README.md#task-2) (`LAB16-CP02`).

**Microsoft Learn sources:**

- [Back up an App Service app](https://learn.microsoft.com/en-us/azure/app-service/manage-backup)

**Source reviewed:** 2026-08-31

## LAB16-Q48 — C

**Question:** The application-platform administrator hardening and protecting a web app needs a safe hardened and recoverable web application change to send outbound application traffic into an approved regional virtual network, followed by web hardening evidence. Which pair merits approval?

- **A — Incorrect.** First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
  First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action. This hardened and recoverable web application pair serves App Service access restrictions. Hardened and recoverable web application closes App Service access restrictions, not regional VNet integration; without the regional VNet integration workflow, it cannot send outbound application traffic into an approved regional virtual network.
- **B — Incorrect.** First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
  First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app. This hardened and recoverable web application pair serves custom-domain DNS records. Custom-domain DNS records cannot replace regional VNet integration in hardened and recoverable web application. Use this regional VNet integration pair instead: First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- **C — Correct.** First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
  First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app. The hardened and recoverable web application uses its regional VNet integration mutation gate and regional VNet integration verification gate before it can send outbound application traffic into an approved regional virtual network.
- **D — Incorrect.** First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. This hardened and recoverable web application pair serves domain ownership verification. Hardened and recoverable web application uses domain ownership verification for both steps; regional VNet integration remains untouched in hardened and recoverable web application, so its regional VNet integration gate to send outbound application traffic into an approved regional virtual network fails.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-3) (`LAB16-CP03`).

**Microsoft Learn sources:**

- [Integrate an App Service app with an Azure virtual network](https://learn.microsoft.com/en-us/azure/app-service/overview-vnet-integration)

**Source reviewed:** 2026-08-31

## LAB16-Q49 — A

**Question:** The hardened and recoverable web application has two web hardening gates: give the application an inbound private address without making integration bidirectional, then prove the hardened and recoverable web application state. Which web hardening sequence works?

- **A — Correct.** First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
  The hardened and recoverable web application gets a complete App Service private endpoints sequence here: first, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address. Read-back evidence follows the change.
- **B — Incorrect.** First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
  First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol. This hardened and recoverable web application pair serves minimum inbound TLS. Hardened and recoverable web application proves minimum inbound TLS, but App Service private endpoints lacks implementation in hardened and recoverable web application and App Service private endpoints proof; the App Service private endpoints outcome to give the application an inbound private address without making integration bidirectional remains open.
- **C — Incorrect.** First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
  First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId. This hardened and recoverable web application pair serves domain ownership verification. Hardened and recoverable web application uses domain ownership verification for both steps; App Service private endpoints remains untouched in hardened and recoverable web application, so its App Service private endpoints gate to give the application an inbound private address without making integration bidirectional fails.
- **D — Incorrect.** First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status. This hardened and recoverable web application pair serves App Service backup storage. Hardened and recoverable web application closes App Service backup storage, not App Service private endpoints; without the App Service private endpoints workflow, it cannot give the application an inbound private address without making integration bidirectional.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-4) (`LAB16-CP04`).

**Microsoft Learn sources:**

- [Use private endpoints for App Service](https://learn.microsoft.com/en-us/azure/app-service/networking/private-endpoint)

**Source reviewed:** 2026-08-31

## LAB16-Q50 — D

**Question:** Which web hardening path makes the hardened and recoverable web application able to allow inbound requests only from approved network sources, then inspects the defining properties?

- **A — Incorrect.** First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
  First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname. This hardened and recoverable web application pair serves HTTPS-only redirection. Hardened and recoverable web application proves HTTPS-only redirection, but App Service access restrictions lacks implementation in hardened and recoverable web application and App Service access restrictions proof; the App Service access restrictions outcome to allow inbound requests only from approved network sources remains open.
- **B — Incorrect.** First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
  First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status. This hardened and recoverable web application pair serves App Service backup storage. Hardened and recoverable web application uses App Service backup storage for both steps; App Service access restrictions remains untouched in hardened and recoverable web application, so its App Service access restrictions gate to allow inbound requests only from approved network sources fails.
- **C — Incorrect.** First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
  First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results. This hardened and recoverable web application pair serves backup schedules and retention. Hardened and recoverable web application closes backup schedules and retention, not App Service access restrictions; without the App Service access restrictions workflow, it cannot allow inbound requests only from approved network sources.
- **D — Correct.** First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
  First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action. This ordered App Service access restrictions workflow lets the hardened and recoverable web application allow inbound requests only from approved network sources and then verify the resulting state.

**Objectives:** `CP-APP-07`

**Remediation:** [Repeat the mapped guided task](../README.md#task-5) (`LAB16-CP05`).

**Microsoft Learn sources:**

- [Set up App Service access restrictions](https://learn.microsoft.com/en-us/azure/app-service/app-service-ip-restrictions)

**Source reviewed:** 2026-08-31
