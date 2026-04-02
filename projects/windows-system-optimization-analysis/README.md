# Windows System Optimization & Performance Analysis

## Objective

The system was experiencing slow performance, likely due to accumulated temporary files, unnecessary startup programs, and potential system integrity issues.

The goal of this project was to diagnose and improve system performance using PowerShell and built-in Windows tools.

---

## Tools Used

* PowerShell
* DISM (Deployment Image Servicing and Management)
* SFC (System File Checker)
* Windows Task Manager
* Built-in Windows utilities

---

## Analysis

Using PowerShell, I analyzed system performance and identified:

* High CPU usage from background applications such as OneDrive, Grammarly, and ChatGPT
* High memory usage from multiple running processes
* Multiple unnecessary startup applications impacting boot time

These findings indicated that system slowdown was primarily caused by resource-heavy background processes and startup bloat.

---

## Actions Taken

* Cleared temporary files using PowerShell
* Removed system temp files to free disk space
* Emptied recycle bin
* Repaired system files using `sfc /scannow`
* Restored Windows image health using `DISM /RestoreHealth`
* Analyzed CPU usage using `Get-Process`
* Analyzed memory usage using `Get-Process`
* Identified unnecessary startup programs
* Reset DNS cache and network stack

---

## Results

* Improved system responsiveness
* Reduced background resource usage
* Freed disk space
* Verified system integrity with no corruption found
* Identified and reduced unnecessary startup processes

---

## Key Takeaway

This project demonstrated that system performance issues are often caused by a combination of software bloat, background processes, and system file health rather than hardware limitations alone.

---

## Future Improvements

* Automate cleanup tasks using a PowerShell script
* Implement scheduled system maintenance
* Monitor performance over time using logging and monitoring tools
