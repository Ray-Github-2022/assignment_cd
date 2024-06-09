[![Run Tests](https://github.com/Ray-Github-2022/assignment_cd/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Ray-Github-2022/assignment_cd/actions/workflows/run-tests.yml)
Use of GitHub Actions workflow to test and -- if it passed -- update the code running on your server after a push..
Continuous Deployment (CD) is the idea of having the product your team is working on be deployed frequently. 

Finally, write a short, 200/300-word report in which you discuss at least the following:
1. Name three components of your solution, explain what they are and how they relate to each other. A 'component' can be anithing from GitHub Actions or Bash to Digital Ocean and SSH.

   Started building fundament of assignment_cd in GitHub (also copied and tested the app in VSC)
   Used Bash for actions/implementing/getting the calculator online => Tested it with IP adress
   
2. Discuss three problems that you encountered along the way and how you solved them.

   First problem: connecting Flask to my calculator.app, unfortunately I received an assertion error
   After running my calculator.py in GitHub next error keeps coming back:
   
   test_calculator.py:15: AssertionError
   FAILED test_calculator.py::test_add - assert b'15.0' 
   ============================== 1 failed in 0.12s ===============================
   Error: Process completed with exit code 1.

   Solution => Adjusted the logic to return only the result in a specific format that the test can verify.
   Code now checks for a query parameter to decide whether to return just the result or the entire HTML page.

   After resolving the issue, I setup the VPS - Digital Ocean. The calculator functions OK

   Lastly I created the SSH key, and saved it in GitHub. I couldn't save it in VPS - Digital Ocean, and didn't understand why..
   => Here I got the remark, invalid public key.. I used: cat ~/.ssh/id_rsa.pub and included the correct id_ xxxxx

   Including below error:
   2024/06/09 10:23:26 ssh.ParsePrivateKey: ssh: no key found
   ======CMD======
   your-deployment-command
   ======END======
   2024/06/09 10:23:26 dial tcp :22: connect: connection refused

   Also I revised the HTML code, after running the updated file in the browser this correctly showed the updated code.

4. (optional) Anything of note that you want to share about the process of solving this assignment.

   Above mentioned "Flask connecting issue" to be explained a bit more => Resolved
   Saving the SSH key in VPS - Digital Ocean => In progress ??
   Also updating files to be explained => Resolved

   Thanks!
