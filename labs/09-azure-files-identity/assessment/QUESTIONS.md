# Lab 09 knowledge check

[Return to the guided lab](../README.md)

Complete all 50 questions before opening the answer key. Allow about 50–60 minutes and choose the single best answer.

Use the result as a learning signal: 85–100% indicates mastery, 70–84% calls for targeted review, and below 70% means repeat the mapped lab tasks before retrying.

## LAB09-Q01 — Foundational

The file-service acceptance architecture note requires the recoverable team file share environment to cap the capacity available to a team file share. Which statement defines the relevant file-service acceptance boundary?

- A. The enabled file-share protocol and account configuration determine which clients and identity options can connect.
- B. For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
- C. An Azure file share quota limits the maximum provisioned capacity for that share.
- D. Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.

## LAB09-Q02 — Foundational

A new file-service acceptance operator must explain why the recoverable team file share can select the file-sharing protocol that matches the client workload. Which explanation is accurate?

- A. The enabled file-share protocol and account configuration determine which clients and identity options can connect.
- B. Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
- C. Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
- D. AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.

## LAB09-Q03 — Foundational

The recoverable team file share acceptance criteria require operators to authenticate file clients with an approved directory identity. Which service fact supports that requirement?

- A. Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
- B. Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
- C. A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
- D. Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.

## LAB09-Q04 — Foundational

A file-service acceptance reviewer challenges whether the recoverable team file share can grant a principal access at the share boundary. Which response resolves the concern?

- A. Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
- B. For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.
- C. Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
- D. An Azure file share quota limits the maximum provisioned capacity for that share.

## LAB09-Q05 — Foundational

The recoverable team file share handoff omits the file-service acceptance rule needed to limit access to particular directories and files after share access is granted. Which statement should the team add?

- A. Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
- B. AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
- C. The enabled file-share protocol and account configuration determine which clients and identity options can connect.
- D. For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.

## LAB09-Q06 — Foundational

A file-service acceptance incident review of the recoverable team file share depends on the ability to restrict share connectivity to the sanctioned route. Which platform description is reliable?

- A. A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
- B. Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.
- C. Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
- D. Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.

## LAB09-Q07 — Foundational

A file-services administrator publishing a recoverable team share is updating the file-service acceptance runbook. The requirement is to capture a point-in-time, read-only view of share contents. Which statement describes Azure behavior correctly?

- A. A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
- B. Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
- C. An Azure file share quota limits the maximum provisioned capacity for that share.
- D. Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.

## LAB09-Q08 — Foundational

A file-service acceptance peer review asks how the recoverable team file share should handle this outcome: restore a share removed during the service retention period. Which explanation is accurate?

- A. AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
- B. The enabled file-share protocol and account configuration determine which clients and identity options can connect.
- C. Soft delete retains a deleted file share for the configured retention period but does not replace file-level snapshots.
- D. For identity-based SMB access, effective authorization combines share-level permission with Windows ACLs.

## LAB09-Q09 — Foundational

For the recoverable team file share, the file-service acceptance plan must transfer file-share content with a resumable command-line data mover. Which statement about file-service acceptance belongs in the recoverable team file share record?

- A. Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.
- B. Identity-based Azure Files authentication replaces account-key authentication for supported SMB clients and directory sources.
- C. AzCopy supports copying files to and from Azure Files when the supplied identity or SAS has sufficient data permissions.
- D. Identity authorization does not bypass storage firewall, private endpoint, DNS, or SMB transport requirements.

## LAB09-Q10 — Foundational

The file-service acceptance review compares four claims for the recoverable team file share requirement to diagnose clients that cannot reach the SMB endpoint on its required port. Which claim is technically sound?

- A. An Azure file share quota limits the maximum provisioned capacity for that share.
- B. Azure Files share-level roles authorize data access at the share scope but do not replace file and directory ACL evaluation.
- C. A share snapshot is a read-only point-in-time copy used to recover prior file and directory content.
- D. Direct SMB mounting commonly requires outbound TCP port 445 unless an alternate connectivity design is used.

## LAB09-Q11 — Foundational

For the recoverable team file share, operators need to cap the capacity available to a team file share. Which change realizes that requirement?

- A. Configure the supported directory source on the storage account before assigning users access.
- B. Provide an approved network path and name resolution in addition to identity permissions.
- C. Authenticate with the least-privilege mechanism and copy a deterministic test directory.
- D. Create the share with an approved quota that fits the account tier and workload forecast.

## LAB09-Q12 — Foundational

Operators must automate the recoverable team file share change needed to select the file-sharing protocol that matches the client workload. Which file-service acceptance operation belongs in the runbook?

- A. Assign the narrowest Storage File Data SMB Share role at the share or account scope.
- B. Create a share snapshot before the controlled file modification in the recovery exercise.
- C. Choose SMB for the identity-based scenario and verify account compatibility before creation.
- D. Test the client-to-file-endpoint network path before troubleshooting storage permissions.

## LAB09-Q13 — Foundational

A recoverable team file share review finds file-service acceptance drift from the need to authenticate file clients with an approved directory identity. Which correction addresses that drift?

- A. Grant both the required share-level role and the minimum NTFS ACL on the target path.
- B. Enable share soft delete before testing deletion of the entire share.
- C. Configure the supported directory source on the storage account before assigning users access.
- D. Create the share with an approved quota that fits the account tier and workload forecast.

## LAB09-Q14 — Foundational

The recoverable team file share window permits only the file-service acceptance change needed to grant a principal access at the share boundary. Which option respects the boundary?

- A. Provide an approved network path and name resolution in addition to identity permissions.
- B. Authenticate with the least-privilege mechanism and copy a deterministic test directory.
- C. Assign the narrowest Storage File Data SMB Share role at the share or account scope.
- D. Choose SMB for the identity-based scenario and verify account compatibility before creation.

## LAB09-Q15 — Foundational

The file-service acceptance preflight has passed; the recoverable team file share must now limit access to particular directories and files after share access is granted. Which operation should run?

- A. Create a share snapshot before the controlled file modification in the recovery exercise.
- B. Grant both the required share-level role and the minimum NTFS ACL on the target path.
- C. Test the client-to-file-endpoint network path before troubleshooting storage permissions.
- D. Configure the supported directory source on the storage account before assigning users access.

## LAB09-Q16 — Applied

The recoverable team file share plan must restrict share connectivity to the sanctioned route while limiting the mutation scope to file-service acceptance. Which action is appropriate?

- A. Provide an approved network path and name resolution in addition to identity permissions.
- B. Enable share soft delete before testing deletion of the entire share.
- C. Create the share with an approved quota that fits the account tier and workload forecast.
- D. Assign the narrowest Storage File Data SMB Share role at the share or account scope.

## LAB09-Q17 — Applied

A file-service acceptance ticket in the recoverable team file share says to capture a point-in-time, read-only view of share contents. Which file-service acceptance action completes the recoverable team file share request with minimal change?

- A. Authenticate with the least-privilege mechanism and copy a deterministic test directory.
- B. Choose SMB for the identity-based scenario and verify account compatibility before creation.
- C. Grant both the required share-level role and the minimum NTFS ACL on the target path.
- D. Create a share snapshot before the controlled file modification in the recovery exercise.

## LAB09-Q18 — Applied

The approach for the recoverable team file share is approved, but the file-service acceptance environment still cannot restore a share removed during the service retention period. Which implementation step closes the gap?

- A. Test the client-to-file-endpoint network path before troubleshooting storage permissions.
- B. Enable share soft delete before testing deletion of the entire share.
- C. Configure the supported directory source on the storage account before assigning users access.
- D. Provide an approved network path and name resolution in addition to identity permissions.

## LAB09-Q19 — Applied

The file-services administrator publishing a recoverable team share may change the recoverable team file share only to transfer file-share content with a resumable command-line data mover. Which file-service acceptance action stays within that assignment?

- A. Authenticate with the least-privilege mechanism and copy a deterministic test directory.
- B. Create the share with an approved quota that fits the account tier and workload forecast.
- C. Assign the narrowest Storage File Data SMB Share role at the share or account scope.
- D. Create a share snapshot before the controlled file modification in the recovery exercise.

## LAB09-Q20 — Applied

A file-service acceptance dry run shows no recoverable team file share command will diagnose clients that cannot reach the SMB endpoint on its required port. Which action belongs before execution?

- A. Choose SMB for the identity-based scenario and verify account compatibility before creation.
- B. Grant both the required share-level role and the minimum NTFS ACL on the target path.
- C. Enable share soft delete before testing deletion of the entire share.
- D. Test the client-to-file-endpoint network path before troubleshooting storage permissions.

## LAB09-Q21 — Applied

The file-services administrator publishing a recoverable team share must confirm the recoverable team file share, without mutation, can cap the capacity available to a team file share. Which file-service acceptance check qualifies?

- A. List the principal's data-role assignment and confirm its scope includes the intended share.
- B. List snapshots and confirm the snapshot timestamp precedes the modification.
- C. Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- D. Query share quota and access tier and compare them with the lab inputs.

## LAB09-Q22 — Applied

The recoverable team file share configuration is complete; the file-service acceptance reviewers need evidence it can select the file-sharing protocol that matches the client workload. Which observation shows success?

- A. Query enabledProtocols and confirm the client uses the matching mount protocol.
- B. Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- C. Query shareDeleteRetentionPolicy and list the deleted share by name.
- D. Query share quota and access tier and compare them with the lab inputs.

## LAB09-Q23 — Applied

The file-service acceptance validation asks whether the recoverable team file share can authenticate file clients with an approved directory identity. Which observable state is strongest?

- A. Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
- B. Query directoryServiceOptions and the account's identity configuration.
- C. Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- D. Query enabledProtocols and confirm the client uses the matching mount protocol.

## LAB09-Q24 — Applied

A recoverable team file share review must prove the file-service acceptance ability to grant a principal access at the share boundary. Which check avoids an adjacent feature?

- A. List snapshots and confirm the snapshot timestamp precedes the modification.
- B. Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- C. List the principal's data-role assignment and confirm its scope includes the intended share.
- D. Query directoryServiceOptions and the account's identity configuration.

## LAB09-Q25 — Applied

The recoverable team file share evidence bundle needs a file-service acceptance result showing it can limit access to particular directories and files after share access is granted. Which result belongs in the checkpoint?

- A. Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- B. Query shareDeleteRetentionPolicy and list the deleted share by name.
- C. Query share quota and access tier and compare them with the lab inputs.
- D. List the principal's data-role assignment and confirm its scope includes the intended share.

## LAB09-Q26 — Applied

Before recoverable team file share cleanup, the file-service acceptance team must reconfirm it can restrict share connectivity to the sanctioned route. Which read-only inspection should run?

- A. Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- B. Query enabledProtocols and confirm the client uses the matching mount protocol.
- C. Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- D. Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.

## LAB09-Q27 — Applied

The recoverable team file share setup reports success after the file-service acceptance attempt to capture a point-in-time, read-only view of share contents. Which file-service acceptance read-only observation proves the recoverable team file share outcome?

- A. Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- B. Query directoryServiceOptions and the account's identity configuration.
- C. List snapshots and confirm the snapshot timestamp precedes the modification.
- D. Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.

## LAB09-Q28 — Applied

The file-service acceptance log says the recoverable team file share can now restore a share removed during the service retention period. Which file-service acceptance state should the recoverable team file share acceptance test retain?

- A. Query share quota and access tier and compare them with the lab inputs.
- B. List the principal's data-role assignment and confirm its scope includes the intended share.
- C. Query shareDeleteRetentionPolicy and list the deleted share by name.
- D. List snapshots and confirm the snapshot timestamp precedes the modification.

## LAB09-Q29 — Applied

The recoverable team file share rejects file-service acceptance exit status as proof it can transfer file-share content with a resumable command-line data mover. Which recoverable team file share result is valid evidence?

- A. Query enabledProtocols and confirm the client uses the matching mount protocol.
- B. Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- C. Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- D. Query shareDeleteRetentionPolicy and list the deleted share by name.

## LAB09-Q30 — Applied

The file-service acceptance validator needs one recoverable team file share query after the change to diagnose clients that cannot reach the SMB endpoint on its required port. Which file-service acceptance property should the recoverable team file share validator inspect?

- A. Query directoryServiceOptions and the account's identity configuration.
- B. Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
- C. Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- D. Compare source and destination file counts, relative paths, lengths, and hashes where supported.

## LAB09-Q31 — Applied

The recoverable team file share result is partial because the file-service acceptance cannot cap the capacity available to a team file share. Which condition accounts for that result?

- A. The share was created for NFS while the validation client attempts an SMB connection.
- B. The principal is authorized, but the client network blocks outbound SMB traffic.
- C. The client network provider blocks outbound TCP 445 to the storage endpoint.
- D. The requested quota exceeds the supported limit for the selected account and share tier.

## LAB09-Q32 — Applied

The file-service acceptance evidence shows the recoverable team file share cannot select the file-sharing protocol that matches the client workload. Which root cause fits that evidence?

- A. The share was created for NFS while the validation client attempts an SMB connection.
- B. The storage account has no configured directory service for SMB identity authentication.
- C. The snapshot was created after the unwanted file change and contains only the changed content.
- D. The requested quota exceeds the supported limit for the selected account and share tier.

## LAB09-Q33 — Applied

Although the recoverable team file share is meant to let the file-service acceptance authenticate file clients with an approved directory identity, its checkpoint fails. Which file-service acceptance defect explains the failure?

- A. The principal has Reader, which grants control-plane visibility but not SMB file data access.
- B. The storage account has no configured directory service for SMB identity authentication.
- C. Soft delete was disabled when the share was removed.
- D. The share was created for NFS while the validation client attempts an SMB connection.

## LAB09-Q34 — Applied

The file-service acceptance support team isolated the recoverable team file share incident to the attempt to grant a principal access at the share boundary. Which condition prevents success?

- A. The user has a share-level role but the directory ACL denies the requested operation.
- B. The SAS omits a permission required to create files in the destination share.
- C. The storage account has no configured directory service for SMB identity authentication.
- D. The principal has Reader, which grants control-plane visibility but not SMB file data access.

## LAB09-Q35 — Applied

A recoverable team file share query surprises the file-services administrator publishing a recoverable team share during the file-service acceptance attempt to limit access to particular directories and files after share access is granted. Which finding explains it?

- A. The principal is authorized, but the client network blocks outbound SMB traffic.
- B. The client network provider blocks outbound TCP 445 to the storage endpoint.
- C. The principal has Reader, which grants control-plane visibility but not SMB file data access.
- D. The user has a share-level role but the directory ACL denies the requested operation.

## LAB09-Q36 — Applied

Other recoverable team file share components are healthy, but the file-service acceptance still cannot restrict share connectivity to the sanctioned route. Which state causes the isolated failure?

- A. The snapshot was created after the unwanted file change and contains only the changed content.
- B. The requested quota exceeds the supported limit for the selected account and share tier.
- C. The principal is authorized, but the client network blocks outbound SMB traffic.
- D. The user has a share-level role but the directory ACL denies the requested operation.

## LAB09-Q37 — Applied

During a file-service acceptance fault drill, the recoverable team file share does not capture a point-in-time, read-only view of share contents. Which finding identifies the defect?

- A. Soft delete was disabled when the share was removed.
- B. The snapshot was created after the unwanted file change and contains only the changed content.
- C. The share was created for NFS while the validation client attempts an SMB connection.
- D. The principal is authorized, but the client network blocks outbound SMB traffic.

## LAB09-Q38 — Applied

The recoverable team file share setup finishes, yet the file-service acceptance cannot restore a share removed during the service retention period. Which misconfiguration explains the mismatch?

- A. The SAS omits a permission required to create files in the destination share.
- B. Soft delete was disabled when the share was removed.
- C. The storage account has no configured directory service for SMB identity authentication.
- D. The snapshot was created after the unwanted file change and contains only the changed content.

## LAB09-Q39 — Applied

A file-service acceptance break/fix in the recoverable team file share fails when operators try to transfer file-share content with a resumable command-line data mover. Which diagnosis fits?

- A. The client network provider blocks outbound TCP 445 to the storage endpoint.
- B. The SAS omits a permission required to create files in the destination share.
- C. The principal has Reader, which grants control-plane visibility but not SMB file data access.
- D. Soft delete was disabled when the share was removed.

## LAB09-Q40 — Applied

The recoverable team file share troubleshooting scope is the file-service acceptance need to diagnose clients that cannot reach the SMB endpoint on its required port. Which condition should be corrected first?

- A. The client network provider blocks outbound TCP 445 to the storage endpoint.
- B. The requested quota exceeds the supported limit for the selected account and share tier.
- C. The user has a share-level role but the directory ACL denies the requested operation.
- D. The SAS omits a permission required to create files in the destination share.

## LAB09-Q41 — Advanced

Which file-service acceptance path makes the recoverable team file share able to cap the capacity available to a team file share, then inspects the defining properties?

- A. First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
- B. First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
- C. First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
- D. First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.

## LAB09-Q42 — Advanced

At the recoverable team file share approval gate, operators must show that the file-service acceptance can select the file-sharing protocol that matches the client workload. Which file-service acceptance configure-and-check pair is defensible?

- A. First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
- B. First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
- C. First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- D. First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.

## LAB09-Q43 — Advanced

The recoverable team file share forbids a partial file-service acceptance result. Operators must first authenticate file clients with an approved directory identity and afterward confirm the recoverable team file share outcome. Which file-service acceptance sequence is complete?

- A. First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- B. First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- C. First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
- D. First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.

## LAB09-Q44 — Advanced

Only the recoverable team file share change needed to grant a principal access at the share boundary is allowed, and file-service acceptance proof is mandatory. Which pair fits?

- A. First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
- B. First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
- C. First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- D. First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.

## LAB09-Q45 — Advanced

The recoverable team file share runbook separates file-service acceptance mutation from validation while it must limit access to particular directories and files after share access is granted. Which sequence proves it cleanly?

- A. First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.
- B. First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- C. First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
- D. First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.

## LAB09-Q46 — Advanced

The recoverable team file share checkpoint requires both this file-service acceptance outcome—restrict share connectivity to the sanctioned route—and a read-only recoverable team file share state check. Which file-service acceptance response is complete?

- A. First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
- B. First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
- C. First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
- D. First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.

## LAB09-Q47 — Advanced

The recoverable team file share runbook must capture a point-in-time, read-only view of share contents, then retain file-service acceptance read-back evidence. Which recoverable team file share pair completes both duties?

- A. First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- B. First, Configure the supported directory source on the storage account before assigning users access. Then, Query directoryServiceOptions and the account's identity configuration.
- C. First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
- D. First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.

## LAB09-Q48 — Advanced

To satisfy the file-service acceptance requirement, operators must change the recoverable team file share configuration and prove it can restore a share removed during the service retention period. Which sequence is coherent?

- A. First, Enable share soft delete before testing deletion of the entire share. Then, Query shareDeleteRetentionPolicy and list the deleted share by name.
- B. First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- C. First, Assign the narrowest Storage File Data SMB Share role at the share or account scope. Then, List the principal's data-role assignment and confirm its scope includes the intended share.
- D. First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.

## LAB09-Q49 — Advanced

The file-services administrator publishing a recoverable team share needs a safe recoverable team file share change to transfer file-share content with a resumable command-line data mover, followed by file-service acceptance evidence. Which pair merits approval?

- A. First, Create the share with an approved quota that fits the account tier and workload forecast. Then, Query share quota and access tier and compare them with the lab inputs.
- B. First, Authenticate with the least-privilege mechanism and copy a deterministic test directory. Then, Compare source and destination file counts, relative paths, lengths, and hashes where supported.
- C. First, Grant both the required share-level role and the minimum NTFS ACL on the target path. Then, Verify the principal's role assignment and inspect the path ACL from a domain-connected client.
- D. First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.

## LAB09-Q50 — Advanced

The recoverable team file share has two file-service acceptance gates: diagnose clients that cannot reach the SMB endpoint on its required port, then prove the recoverable team file share state. Which file-service acceptance sequence works?

- A. First, Choose SMB for the identity-based scenario and verify account compatibility before creation. Then, Query enabledProtocols and confirm the client uses the matching mount protocol.
- B. First, Test the client-to-file-endpoint network path before troubleshooting storage permissions. Then, Resolve the endpoint and test TCP 445 independently of the SMB sign-in attempt.
- C. First, Provide an approved network path and name resolution in addition to identity permissions. Then, Resolve the file endpoint, test TCP 445 where applicable, and then validate SMB identity access.
- D. First, Create a share snapshot before the controlled file modification in the recovery exercise. Then, List snapshots and confirm the snapshot timestamp precedes the modification.

[Open the answer key](./ANSWERS.md)
