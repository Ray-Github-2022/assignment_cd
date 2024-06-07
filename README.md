[![Run Tests](https://github.com/Ray-Github-2022/assignment_cd/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Ray-Github-2022/assignment_cd/actions/workflows/run-tests.yml)
Continuous Deployment (CD) is the idea of having the product your team is working on be deployed frequently. Use of GitHub Actions workflow to test and -- if it passed -- update the code running on your server after a push..

Finally, write a short, 200/300-word report in which you discuss at least the following:
1. Name three components of your solution, explain what they are and how they relate to each other. 
   A 'component' can be anthing from GitHub Actions or Bash to Digital Ocean and SSH.

   Started building fundament of assignment_cd in GitHub (also copied and tested the app in VSC)
   Used Bash for actions/implementing/getting the calculator online => Tested it with IP adress
   
2. Discuss three problems that you encountered along the way and how you solved them.

   First problem: connecting Flask to my calculator.app without receiving errors =>

After running my calculator.py in GitHub next error keeps coming back: FAILED test_calculator.py::test_add - assert b'15.0' in b'\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=de..."><b>=</b></button>\n        </form>\n        \n        <h3>Outcome: None</h3>\n        \n    </div>\n</body>\n</html>'
 +  where b'\n<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=de..."><b>=</b></button>\n        </form>\n        \n        <h3>Outcome: None</h3>\n        \n    </div>\n</body>\n</html>' = <WrapperTestResponse 3045 bytes [200 OK]>.data
============================== 1 failed in 0.12s ===============================
Error: Process completed with exit code 1.

   Before resolving the issue, I setup the VPS - Digital Ocean. All functions OK
   After that I couldn't resolve the issue with Flask on GitHub Testing, what should I change here / what is wrong?
   Lastly I created the SSH key, and saved it in GitHub. I couldn't save it in VPS - Digital Ocean, and didn't understand why..
   => Here I got the remark, invalid key.. I used: cat ~/.ssh/id_rsa.pub and included the correct id_ xxxxx

   Also I updated the HTML code, after running the uodated file in the brwoser it didn't show the updated code?

4. (optional) Anything of note that you want to share about the process of solving this assignment.

   Above mentioned "Flask connecting issue" to be explained a bit more..
   Same as saving the SSH key in VPS - Digital Ocean
   Also updating files to be explained

   Thanks!
