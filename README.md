# Project Explanation
  Preparing tender documentation is hard. It takes too much time to collect every file in order and it is mostly routine job to do. So, I thought it will be great if
I write a Python code to decrease automation process. Normal routine is taking these steps:

  1. Filling new files (not routine files).
  2. Copying existing files (routine).
  3. Print or Rar the whole files (routine).
  4. Send it to the customer/manager (routine).
  
  It might seem short but first and second step is very painful to do. We can not do anything for first step at the moment but I think I can solve my other problems. Let's
divide my problems in details. In second step I will require catalogues, equipment list, equipment datasheets, ISO certificates (9001, 14001, 50001), IEC Certificates
(17025E), similar test reports, references (according to project country and product type), company profile, financial documents (partly for years), shareholders
documents, company registration documents, offer letter, tender L/C if required, QHSE document, HSE statistics, spare parts list, Datasheets and Drawings. These files
will be in the screen as check boxes. After choosing country and writing project name it could be checkable for every item above. 
  
  In the third step User will choose necessary files and program will add all checked files to the rar. If rar file size is too big (90% chance), program will upload it
to the Wetransfer and copy the Wetransfer link.

  In the fourth step, program will open Outlook and send an email to writen address. CC will be optional in new versions.
  
  I plan to use Python and Tkinter for the project. GUI is will be faster than just use as script.
  
  DISCLAIMER: This is written by a new software developer. While using this program please consider this and check every step manually.
  

# 2023-01-17-01-documentation-automation
Arranging Github and Wakatime to track project in more pro way.
