# Lab 16 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB16-Q01 — Foundational

A new web hardening operator must explain why the hardened and recoverable web application can reject inbound clients that negotiate a protocol below the approved TLS version. Which explanation is accurate?

- A. Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
- B. The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
- C. App Service requires proof of custom-domain ownership before binding the hostname.
- D. App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.

## LAB16-Q02 — Foundational

The hardened and recoverable web application acceptance criteria require operators to redirect unencrypted application requests to HTTPS. Which service fact supports that requirement?

- A. An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
- B. Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
- C. App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
- D. An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.

## LAB16-Q03 — Foundational

A web hardening reviewer challenges whether the hardened and recoverable web application can bind a supported platform-managed certificate to a custom hostname. Which response resolves the concern?

- A. A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
- B. An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
- C. The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
- D. Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.

## LAB16-Q04 — Foundational

The hardened and recoverable web application handoff omits the web hardening rule needed to publish the record type required for the chosen custom hostname. Which statement should the team add?

- A. App Service requires proof of custom-domain ownership before binding the hostname.
- B. App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
- C. The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
- D. A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.

## LAB16-Q05 — Foundational

A web hardening incident review of the hardened and recoverable web application depends on the ability to prove control of a hostname before binding it to the application. Which platform description is reliable?

- A. App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.
- B. An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
- C. Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
- D. App Service requires proof of custom-domain ownership before binding the hostname.

## LAB16-Q06 — Foundational

An application-platform administrator hardening and protecting a web app is updating the web hardening runbook. The requirement is to write application backups to an authorized storage destination. Which statement describes Azure behavior correctly?

- A. The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
- B. Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
- C. An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
- D. App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.

## LAB16-Q07 — Foundational

A web hardening peer review asks how the hardened and recoverable web application should handle this outcome: retain scheduled backups for the required recovery window. Which explanation is accurate?

- A. The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
- B. App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.
- C. The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
- D. A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.

## LAB16-Q08 — Foundational

For the hardened and recoverable web application, the web hardening plan must send outbound application traffic into an approved regional virtual network. Which statement about web hardening belongs in the hardened and recoverable web application record?

- A. An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
- B. Enabling HTTPS Only redirects ordinary HTTP requests to HTTPS but does not itself bind a custom certificate.
- C. App Service requires proof of custom-domain ownership before binding the hostname.
- D. App Service VNet integration gives the app outbound access through a delegated integration subnet; it does not make inbound traffic private.

## LAB16-Q09 — Foundational

The web hardening review compares four claims for the hardened and recoverable web application requirement to give the application an inbound private address without making integration bidirectional. Which claim is technically sound?

- A. Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.
- B. An App Service private endpoint provides inbound private connectivity and requires correct private DNS resolution.
- C. An App Service managed certificate can cover eligible custom domains but has feature and validation limitations.
- D. App Service backups write to a Blob container authorized by a storage SAS and can include supported app configuration and data.

## LAB16-Q10 — Foundational

The web hardening architecture note requires the hardened and recoverable web application environment to allow inbound requests only from approved network sources. Which statement defines the relevant web hardening boundary?

- A. The App Service minimum TLS setting rejects client handshakes below the configured protocol version.
- B. A subdomain commonly maps by CNAME to the app hostname, while an apex domain typically uses supported A and TXT validation records.
- C. The backup schedule controls frequency and retention, subject to App Service tier and platform limits.
- D. Access restrictions evaluate ordered allow and deny rules for inbound traffic before requests reach the app.

## LAB16-Q11 — Foundational

Operators must automate the hardened and recoverable web application change needed to reject inbound clients that negotiate a protocol below the approved TLS version. Which web hardening operation belongs in the runbook?

- A. Set minTlsVersion to the approved baseline and confirm application clients support it.
- B. Validate domain ownership and request the managed certificate only for a supported hostname and plan.
- C. Create a private backup container and provide a short-lived SAS with the permissions required by backup.
- D. Create the private endpoint, approve its connection, and link the correct private DNS zone.

## LAB16-Q12 — Foundational

A hardened and recoverable web application review finds web hardening drift from the need to redirect unencrypted application requests to HTTPS. Which correction addresses that drift?

- A. Create the required DNS record type and preserve the ownership-verification record.
- B. Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
- C. Configure a supported frequency, start time, and retention period that meets recovery requirements.
- D. Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.

## LAB16-Q13 — Foundational

The hardened and recoverable web application window permits only the web hardening change needed to bind a supported platform-managed certificate to a custom hostname. Which option respects the boundary?

- A. Publish the required asuid TXT record or supported validation record before adding the binding.
- B. Integrate the app with a dedicated delegated subnet for outbound private-resource access.
- C. Validate domain ownership and request the managed certificate only for a supported hostname and plan.
- D. Set minTlsVersion to the approved baseline and confirm application clients support it.

## LAB16-Q14 — Foundational

The web hardening preflight has passed; the hardened and recoverable web application must now publish the record type required for the chosen custom hostname. Which operation should run?

- A. Create a private backup container and provide a short-lived SAS with the permissions required by backup.
- B. Create the required DNS record type and preserve the ownership-verification record.
- C. Create the private endpoint, approve its connection, and link the correct private DNS zone.
- D. Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.

## LAB16-Q15 — Foundational

The hardened and recoverable web application plan must prove control of a hostname before binding it to the application while limiting the mutation scope to web hardening. Which action is appropriate?

- A. Configure a supported frequency, start time, and retention period that meets recovery requirements.
- B. Publish the required asuid TXT record or supported validation record before adding the binding.
- C. Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
- D. Validate domain ownership and request the managed certificate only for a supported hostname and plan.

## LAB16-Q16 — Applied

A web hardening ticket in the hardened and recoverable web application says to write application backups to an authorized storage destination. Which web hardening action completes the hardened and recoverable web application request with minimal change?

- A. Integrate the app with a dedicated delegated subnet for outbound private-resource access.
- B. Set minTlsVersion to the approved baseline and confirm application clients support it.
- C. Create the required DNS record type and preserve the ownership-verification record.
- D. Create a private backup container and provide a short-lived SAS with the permissions required by backup.

## LAB16-Q17 — Applied

The approach for the hardened and recoverable web application is approved, but the web hardening environment still cannot retain scheduled backups for the required recovery window. Which implementation step closes the gap?

- A. Create the private endpoint, approve its connection, and link the correct private DNS zone.
- B. Configure a supported frequency, start time, and retention period that meets recovery requirements.
- C. Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
- D. Publish the required asuid TXT record or supported validation record before adding the binding.

## LAB16-Q18 — Applied

The application-platform administrator hardening and protecting a web app may change the hardened and recoverable web application only to send outbound application traffic into an approved regional virtual network. Which web hardening action stays within that assignment?

- A. Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.
- B. Validate domain ownership and request the managed certificate only for a supported hostname and plan.
- C. Integrate the app with a dedicated delegated subnet for outbound private-resource access.
- D. Create a private backup container and provide a short-lived SAS with the permissions required by backup.

## LAB16-Q19 — Applied

A web hardening dry run shows no hardened and recoverable web application command will give the application an inbound private address without making integration bidirectional. Which action belongs before execution?

- A. Set minTlsVersion to the approved baseline and confirm application clients support it.
- B. Create the required DNS record type and preserve the ownership-verification record.
- C. Create the private endpoint, approve its connection, and link the correct private DNS zone.
- D. Configure a supported frequency, start time, and retention period that meets recovery requirements.

## LAB16-Q20 — Applied

For the hardened and recoverable web application, operators need to allow inbound requests only from approved network sources. Which change realizes that requirement?

- A. Enable httpsOnly and configure a certificate binding separately for each protected custom hostname.
- B. Publish the required asuid TXT record or supported validation record before adding the binding.
- C. Integrate the app with a dedicated delegated subnet for outbound private-resource access.
- D. Add narrowly scoped allow rules and retain an intentional unmatched-traffic action.

## LAB16-Q21 — Applied

The hardened and recoverable web application configuration is complete; the web hardening reviewers need evidence it can reject inbound clients that negotiate a protocol below the approved TLS version. Which observation shows success?

- A. Resolve the public record and query custom hostnames on the app.
- B. Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- C. Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- D. Query rule priorities, actions, source ranges, service tags, and unmatched action.

## LAB16-Q22 — Applied

The web hardening validation asks whether the hardened and recoverable web application can redirect unencrypted application requests to HTTPS. Which observable state is strongest?

- A. Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- B. Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- C. Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- D. Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.

## LAB16-Q23 — Applied

A hardened and recoverable web application review must prove the web hardening ability to bind a supported platform-managed certificate to a custom hostname. Which check avoids an adjacent feature?

- A. Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- B. Resolve the app hostname privately and query the endpoint connection state and NIC address.
- C. Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- D. Query httpsOnly and inspect hostNameSslStates for the custom hostname.

## LAB16-Q24 — Applied

The hardened and recoverable web application evidence bundle needs a web hardening result showing it can publish the record type required for the chosen custom hostname. Which result belongs in the checkpoint?

- A. Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- B. Resolve the public record and query custom hostnames on the app.
- C. Query rule priorities, actions, source ranges, service tags, and unmatched action.
- D. Query certificate expiration, thumbprint, hostname, and the app's SNI binding.

## LAB16-Q25 — Applied

Before hardened and recoverable web application cleanup, the web hardening team must reconfirm it can prove control of a hostname before binding it to the application. Which read-only inspection should run?

- A. Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- B. Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- C. Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- D. Resolve the public record and query custom hostnames on the app.

## LAB16-Q26 — Applied

The hardened and recoverable web application setup reports success after the web hardening attempt to write application backups to an authorized storage destination. Which web hardening read-only observation proves the hardened and recoverable web application outcome?

- A. Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- B. Resolve the app hostname privately and query the endpoint connection state and NIC address.
- C. Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- D. Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.

## LAB16-Q27 — Applied

The web hardening log says the hardened and recoverable web application can now retain scheduled backups for the required recovery window. Which web hardening state should the hardened and recoverable web application acceptance test retain?

- A. Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- B. Query rule priorities, actions, source ranges, service tags, and unmatched action.
- C. Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- D. Query backup configuration, storage URL redaction, enabled state, and the latest backup status.

## LAB16-Q28 — Applied

The hardened and recoverable web application rejects web hardening exit status as proof it can send outbound application traffic into an approved regional virtual network. Which hardened and recoverable web application result is valid evidence?

- A. Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- B. Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- C. Resolve the public record and query custom hostnames on the app.
- D. Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.

## LAB16-Q29 — Applied

The web hardening validator needs one hardened and recoverable web application query after the change to give the application an inbound private address without making integration bidirectional. Which web hardening property should the hardened and recoverable web application validator inspect?

- A. Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- B. Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- C. Resolve the app hostname privately and query the endpoint connection state and NIC address.
- D. Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.

## LAB16-Q30 — Applied

The application-platform administrator hardening and protecting a web app must confirm the hardened and recoverable web application, without mutation, can allow inbound requests only from approved network sources. Which web hardening check qualifies?

- A. Query rule priorities, actions, source ranges, service tags, and unmatched action.
- B. Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- C. Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- D. Resolve the app hostname privately and query the endpoint connection state and NIC address.

## LAB16-Q31 — Applied

The web hardening evidence shows the hardened and recoverable web application cannot reject inbound clients that negotiate a protocol below the approved TLS version. Which root cause fits that evidence?

- A. HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
- B. The SAS expired before the scheduled backup attempted to write its archive.
- C. A broad deny rule has a higher priority than the required allow rule.
- D. A legacy client negotiates only a TLS version below the app's minimum.

## LAB16-Q32 — Applied

Although the hardened and recoverable web application is meant to let the web hardening redirect unencrypted application requests to HTTPS, its checkpoint fails. Which web hardening defect explains the failure?

- A. The requested hostname or DNS configuration is not eligible for a managed certificate.
- B. HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
- C. The selected plan tier does not support the required automated backup feature.
- D. A legacy client negotiates only a TLS version below the app's minimum.

## LAB16-Q33 — Applied

The web hardening support team isolated the hardened and recoverable web application incident to the attempt to bind a supported platform-managed certificate to a custom hostname. Which condition prevents success?

- A. The CNAME points to a deployment-slot hostname that is not the approved production target.
- B. The requested hostname or DNS configuration is not eligible for a managed certificate.
- C. The design expects VNet integration alone to remove the public inbound endpoint.
- D. HTTPS Only is enabled, but the custom hostname has no valid certificate binding.

## LAB16-Q34 — Applied

A hardened and recoverable web application query surprises the application-platform administrator hardening and protecting a web app during the web hardening attempt to publish the record type required for the chosen custom hostname. Which finding explains it?

- A. The CNAME points to a deployment-slot hostname that is not the approved production target.
- B. The TXT record was created under the wrong DNS label.
- C. DNS still resolves the app hostname to its public endpoint from inside the virtual network.
- D. The requested hostname or DNS configuration is not eligible for a managed certificate.

## LAB16-Q35 — Applied

Other hardened and recoverable web application components are healthy, but the web hardening still cannot prove control of a hostname before binding it to the application. Which state causes the isolated failure?

- A. The SAS expired before the scheduled backup attempted to write its archive.
- B. A broad deny rule has a higher priority than the required allow rule.
- C. The CNAME points to a deployment-slot hostname that is not the approved production target.
- D. The TXT record was created under the wrong DNS label.

## LAB16-Q36 — Applied

During a web hardening fault drill, the hardened and recoverable web application does not write application backups to an authorized storage destination. Which finding identifies the defect?

- A. The selected plan tier does not support the required automated backup feature.
- B. A legacy client negotiates only a TLS version below the app's minimum.
- C. The TXT record was created under the wrong DNS label.
- D. The SAS expired before the scheduled backup attempted to write its archive.

## LAB16-Q37 — Applied

The hardened and recoverable web application setup finishes, yet the web hardening cannot retain scheduled backups for the required recovery window. Which misconfiguration explains the mismatch?

- A. The design expects VNet integration alone to remove the public inbound endpoint.
- B. HTTPS Only is enabled, but the custom hostname has no valid certificate binding.
- C. The selected plan tier does not support the required automated backup feature.
- D. The SAS expired before the scheduled backup attempted to write its archive.

## LAB16-Q38 — Applied

A web hardening break/fix in the hardened and recoverable web application fails when operators try to send outbound application traffic into an approved regional virtual network. Which diagnosis fits?

- A. DNS still resolves the app hostname to its public endpoint from inside the virtual network.
- B. The requested hostname or DNS configuration is not eligible for a managed certificate.
- C. The design expects VNet integration alone to remove the public inbound endpoint.
- D. The selected plan tier does not support the required automated backup feature.

## LAB16-Q39 — Applied

The hardened and recoverable web application troubleshooting scope is the web hardening need to give the application an inbound private address without making integration bidirectional. Which condition should be corrected first?

- A. A broad deny rule has a higher priority than the required allow rule.
- B. The CNAME points to a deployment-slot hostname that is not the approved production target.
- C. DNS still resolves the app hostname to its public endpoint from inside the virtual network.
- D. The design expects VNet integration alone to remove the public inbound endpoint.

## LAB16-Q40 — Applied

The hardened and recoverable web application result is partial because the web hardening cannot allow inbound requests only from approved network sources. Which condition accounts for that result?

- A. A broad deny rule has a higher priority than the required allow rule.
- B. A legacy client negotiates only a TLS version below the app's minimum.
- C. The TXT record was created under the wrong DNS label.
- D. DNS still resolves the app hostname to its public endpoint from inside the virtual network.

## LAB16-Q41 — Advanced

At the hardened and recoverable web application approval gate, operators must show that the web hardening can reject inbound clients that negotiate a protocol below the approved TLS version. Which web hardening configure-and-check pair is defensible?

- A. First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- B. First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- C. First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- D. First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.

## LAB16-Q42 — Advanced

The hardened and recoverable web application forbids a partial web hardening result. Operators must first redirect unencrypted application requests to HTTPS and afterward confirm the hardened and recoverable web application outcome. Which web hardening sequence is complete?

- A. First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
- B. First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- C. First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- D. First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.

## LAB16-Q43 — Advanced

Only the hardened and recoverable web application change needed to bind a supported platform-managed certificate to a custom hostname is allowed, and web hardening proof is mandatory. Which pair fits?

- A. First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- B. First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- C. First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
- D. First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.

## LAB16-Q44 — Advanced

The hardened and recoverable web application runbook separates web hardening mutation from validation while it must publish the record type required for the chosen custom hostname. Which sequence proves it cleanly?

- A. First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
- B. First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- C. First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
- D. First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.

## LAB16-Q45 — Advanced

The hardened and recoverable web application checkpoint requires both this web hardening outcome—prove control of a hostname before binding it to the application—and a read-only hardened and recoverable web application state check. Which web hardening response is complete?

- A. First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- B. First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- C. First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- D. First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.

## LAB16-Q46 — Advanced

The hardened and recoverable web application runbook must write application backups to an authorized storage destination, then retain web hardening read-back evidence. Which hardened and recoverable web application pair completes both duties?

- A. First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- B. First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- C. First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- D. First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.

## LAB16-Q47 — Advanced

To satisfy the web hardening requirement, operators must change the hardened and recoverable web application configuration and prove it can retain scheduled backups for the required recovery window. Which sequence is coherent?

- A. First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
- B. First, Validate domain ownership and request the managed certificate only for a supported hostname and plan. Then, Query certificate expiration, thumbprint, hostname, and the app's SNI binding.
- C. First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
- D. First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.

## LAB16-Q48 — Advanced

The application-platform administrator hardening and protecting a web app needs a safe hardened and recoverable web application change to send outbound application traffic into an approved regional virtual network, followed by web hardening evidence. Which pair merits approval?

- A. First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.
- B. First, Create the required DNS record type and preserve the ownership-verification record. Then, Resolve the public record and query custom hostnames on the app.
- C. First, Integrate the app with a dedicated delegated subnet for outbound private-resource access. Then, Query virtualNetworkSubnetId and test outbound resolution and connectivity from the app.
- D. First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.

## LAB16-Q49 — Advanced

The hardened and recoverable web application has two web hardening gates: give the application an inbound private address without making integration bidirectional, then prove the hardened and recoverable web application state. Which web hardening sequence works?

- A. First, Create the private endpoint, approve its connection, and link the correct private DNS zone. Then, Resolve the app hostname privately and query the endpoint connection state and NIC address.
- B. First, Set minTlsVersion to the approved baseline and confirm application clients support it. Then, Query siteConfig.minTlsVersion and test a supported and an obsolete client protocol.
- C. First, Publish the required asuid TXT record or supported validation record before adding the binding. Then, Resolve the TXT record and confirm its value matches the app's customDomainVerificationId.
- D. First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.

## LAB16-Q50 — Advanced

Which web hardening path makes the hardened and recoverable web application able to allow inbound requests only from approved network sources, then inspects the defining properties?

- A. First, Enable httpsOnly and configure a certificate binding separately for each protected custom hostname. Then, Query httpsOnly and inspect hostNameSslStates for the custom hostname.
- B. First, Create a private backup container and provide a short-lived SAS with the permissions required by backup. Then, Query backup configuration, storage URL redaction, enabled state, and the latest backup status.
- C. First, Configure a supported frequency, start time, and retention period that meets recovery requirements. Then, Query backup schedule frequency, retentionPeriodInDays, keepAtLeastOneBackup, and recent results.
- D. First, Add narrowly scoped allow rules and retain an intentional unmatched-traffic action. Then, Query rule priorities, actions, source ranges, service tags, and unmatched action.

[Open the answer key](./ANSWERS.md)
