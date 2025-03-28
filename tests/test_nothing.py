{
  "id": "63d6e3a9-0a03-4ed8-bd58-59125739e46c",
  "version": "2.0",
  "name": "SmokeTest",
  "url": "http://127.0.0.1:5001/teton/1.6/index.html",
  "tests": [{
    "id": "30fc6cb3-0ccf-4989-be3b-684318ecc12c",
    "name": "smoke2",
    "commands": [{
      "id": "6fe96875-cced-40d7-a5fa-7f9bf2fc7ecc",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5001/teton/1.6/join.html",
      "targets": [],
      "value": ""
    }, {
      "id": "ad968846-317b-4744-8fe5-67e371008f20",
      "comment": "",
      "command": "setWindowSize",
      "target": "739x696",
      "targets": [],
      "value": ""
    }, {
      "id": "222810fa-1cb1-406b-aef4-aba37fd8de7a",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-equiv > img",
      "targets": [
        ["css=#hamburger-equiv > img", "css:finder"],
        ["xpath=//img[@alt='Hamburger menu open']", "xpath:img"],
        ["xpath=//span[@id='hamburger-equiv']/img", "xpath:idRelative"],
        ["xpath=//span[2]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d8d56c66-0e78-443a-809c-46978e45739b",
      "comment": "",
      "command": "click",
      "target": "linkText=Home",
      "targets": [
        ["linkText=Home", "linkText"],
        ["css=li:nth-child(1) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Home')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'index.html')])[2]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Home')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "9c73eb20-3147-4315-8063-854eb2dec3a8",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.header-logo img",
      "targets": [
        ["css=.header-logo img", "css:finder"],
        ["xpath=//img[@alt='Teton Chamber of Commerce Logo']", "xpath:img"],
        ["xpath=//div[@id='content']/header/div/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "07f9cf00-67b6-4bab-9894-77a81dcae255",
      "comment": "",
      "command": "verifyText",
      "target": "css=.header-title > h1",
      "targets": [
        ["css=.header-title > h1", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h1", "xpath:idRelative"],
        ["xpath=//h1", "xpath:position"],
        ["xpath=//h1[contains(.,'Teton Idaho')]", "xpath:innerText"]
      ],
      "value": "Teton Idaho"
    }, {
      "id": "bdd46801-1fa5-4100-a169-520a1e63993d",
      "comment": "",
      "command": "verifyText",
      "target": "css=.header-title > h2",
      "targets": [
        ["css=.header-title > h2", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h2", "xpath:idRelative"],
        ["xpath=//h2", "xpath:position"],
        ["xpath=//h2[contains(.,'Chamber of Commerce')]", "xpath:innerText"]
      ],
      "value": "Chamber of Commerce"
    }, {
      "id": "dca49ef7-6757-46b2-98e8-83720e9dbd19",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 img",
      "targets": [
        ["css=.spotlight1 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p/a/img", "xpath:idRelative"],
        ["xpath=//p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ac6d9db9-e0cb-43d6-928d-b13f320a72fc",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 img",
      "targets": [
        ["css=.spotlight2 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p/a/img", "xpath:idRelative"],
        ["xpath=//div[2]/p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "43a04385-1194-49c4-833c-1151ef941707",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "940fac10-a566-4bc4-a69c-4658a66e2087",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "62be609e-767c-42ed-970d-9b72b8023f38",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6c62f2b8-0335-4584-a6e2-e972da1ad6e1",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "Zackary"
    }, {
      "id": "aa3c9f0f-0d7c-48f1-9571-bf217b1487a6",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f84d5601-82bc-400c-b60a-e7f6390f2993",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "3f60d7b8-7797-4d7c-86d6-145f506e7f99",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "Sinclair"
    }, {
      "id": "39903f5c-4a66-445a-9fd3-bb7be650bc42",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eb787112-5254-4f75-8682-6749e0c977c4",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6ae477ae-89e1-4edb-875a-b4333ff941a9",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "Sinclair Solutions"
    }, {
      "id": "b4f911f3-2470-4208-bde3-aaa30618cc20",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c9c00546-6528-4aee-bc5d-867bf0baebb1",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1f1c8cda-5f52-4ff1-b664-4ed5d74f0471",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "85eebdab-2413-46ce-b5c2-caf1a815a706",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "Problem Solver"
    }, {
      "id": "a6f85d19-1963-4357-aaf6-1cbd6d00876d",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9ef63b28-a1bf-4759-a422-794f82a513fd",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a8f5a4ab-b5f6-49dc-b4dc-651dee1f6f9c",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9927e8c2-3587-4d7c-a83a-7a87c33975dc",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-equiv > img",
      "targets": [
        ["css=#hamburger-equiv > img", "css:finder"],
        ["xpath=//span[@id='hamburger-equiv']/img", "xpath:idRelative"],
        ["xpath=//span[2]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b15dac3b-3698-41fe-918c-b31c3caa37b2",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-x > img",
      "targets": [
        ["css=#hamburger-x > img", "css:finder"],
        ["xpath=//span[@id='hamburger-x']/img", "xpath:idRelative"],
        ["xpath=//span/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a82f32f5-adc1-4067-885f-af6b2000f4fb",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-equiv > img",
      "targets": [
        ["css=#hamburger-equiv > img", "css:finder"],
        ["xpath=//span[@id='hamburger-equiv']/img", "xpath:idRelative"],
        ["xpath=//span[2]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e3f3a0a6-5a9d-43ea-ba2d-411c771546dc",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "2574fcb3-e52b-4ff1-abd3-48c90daec630",
      "comment": "",
      "command": "click",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "58673e26-7a49-45b7-92ea-5ac9bc14055f",
      "comment": "",
      "command": "doubleClick",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "ba11f5fc-f4c4-4c6a-9989-fa3c6f47512b",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.gold-member:nth-child(9) > img",
      "targets": [
        ["css=.gold-member:nth-child(9) > img", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/img", "xpath:idRelative"],
        ["xpath=//section[9]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "1035bb4e-168c-40d4-b6d4-ea3656a81230",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b0e4bea0-65b9-4346-8c5f-b298f6959d34",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "dd4b4a9d-284f-47ef-a68b-69395c1e0572",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "a601bfe7-e856-4397-8db6-6e5009a8de51",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-equiv > img",
      "targets": [
        ["css=#hamburger-equiv > img", "css:finder"],
        ["xpath=(//img[@alt='hamburger menu image'])[2]", "xpath:img"],
        ["xpath=//span[@id='hamburger-equiv']/img", "xpath:idRelative"],
        ["xpath=//span[2]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "fa089c93-2be7-455e-a13c-f4a8f625a49c",
      "comment": "",
      "command": "click",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "4c439b72-111f-4602-932e-7eb6c09ce1b3",
      "comment": "",
      "command": "click",
      "target": "css=#hamburger-equiv > img",
      "targets": [
        ["css=#hamburger-equiv > img", "css:finder"],
        ["xpath=//img[@alt='Hamburger menu open']", "xpath:img"],
        ["xpath=//span[@id='hamburger-equiv']/img", "xpath:idRelative"],
        ["xpath=//span[2]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a9dffe12-a5dd-4c46-aae8-7ce06451903c",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "60b00fad-7c00-40f0-a7e0-74feb1d6c5d4",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b66ea74b-69cc-4948-8f8a-dd8f1789b20d",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b5558ad0-b734-4f38-9d34-3a1defb3e68a",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "093062d8-06d3-4e44-91e3-91cce144b507",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "invalid"
    }, {
      "id": "11c43820-96e2-4f94-b1b2-11dd4f4ed0b5",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "87878893-c16c-47cc-9000-ccd0502a4794",
      "comment": "",
      "command": "click",
      "target": "css=.admin-main",
      "targets": [
        ["css=.admin-main", "css:finder"],
        ["xpath=//div[@id='content']/main", "xpath:idRelative"],
        ["xpath=//main", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "65addda8-34f7-401d-b7e7-fb7c5637d3af",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7c7f3256-d9f4-43ca-be72-64a9f2275945",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b9572e54-71d5-4554-adb8-21a1d54cbb6a",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "passowrd"
    }, {
      "id": "24d27d18-e389-41d4-93fa-2fd8e55cea25",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "bb4ffe77-6f73-4122-a8f8-6e593f65a872",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.errorMessage",
      "targets": [
        ["css=.errorMessage", "css:finder"],
        ["xpath=//div[@id='content']/main/section/form/div/span", "xpath:idRelative"],
        ["xpath=//div/span", "xpath:position"],
        ["xpath=//span[contains(.,'Invalid username and password.')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "359efb93-e517-4fa2-9eff-cacb12bc745b",
      "comment": "",
      "command": "click",
      "target": "css=.footer-content",
      "targets": [
        ["css=.footer-content", "css:finder"],
        ["xpath=//div[@id='content']/footer/div", "xpath:idRelative"],
        ["xpath=//footer/div", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "3694914e-9eec-451c-9661-791d812d5cd1",
    "name": "Admin Page",
    "commands": [{
      "id": "5f180162-9b04-4285-85d6-0108ff159249",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5001/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "92838a0f-9427-4538-84d8-53fd3905b951",
      "comment": "",
      "command": "setWindowSize",
      "target": "1198x697",
      "targets": [],
      "value": ""
    }, {
      "id": "6cdef534-863e-4311-9c02-1b494c0d8689",
      "comment": "",
      "command": "click",
      "target": "linkText=Admin",
      "targets": [
        ["linkText=Admin", "linkText"],
        ["css=li:nth-child(4) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Admin')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[4]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'admin.html')]", "xpath:href"],
        ["xpath=//li[4]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Admin')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "df5487b2-6d6e-4a4d-97e2-b3529120f0f2",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "83fd256a-0e1d-4cf3-aba1-671670a60369",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "702bd107-748c-4e62-8137-c527af914893",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "username:"
    }, {
      "id": "ad0f2945-b452-4278-be84-80844aeede15",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "800be9f2-bf35-4f3a-991f-391e9ba7bd08",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9a4d340b-3481-449c-93ca-8e67e9882694",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "password"
    }, {
      "id": "83621095-ae12-43c4-ba1f-cbebff2a2b00",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "6e61c33f-e1b0-4bbc-9e3c-77ba09510eb1",
    "name": "Directory Page",
    "commands": [{
      "id": "20f5f56b-6798-4643-94e8-90f804fa0238",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5001/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "77b290ce-af33-46ab-a6a4-61ef16633019",
      "comment": "",
      "command": "setWindowSize",
      "target": "1198x697",
      "targets": [],
      "value": ""
    }, {
      "id": "515b1448-d5f7-4fd2-be0c-4b91de9ac1c7",
      "comment": "",
      "command": "click",
      "target": "linkText=Directory",
      "targets": [
        ["linkText=Directory", "linkText"],
        ["css=li:nth-child(3) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Directory')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[3]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'directory.html')]", "xpath:href"],
        ["xpath=//li[3]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Directory')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "9434fa94-9111-4458-a4e9-a10e02c8ab42",
      "comment": "",
      "command": "assertElementPresent",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d1971b2a-0fdb-44b1-8265-5d60748866ad",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.gold-member:nth-child(9) > img",
      "targets": [
        ["css=.gold-member:nth-child(9) > img", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/img", "xpath:idRelative"],
        ["xpath=//section[9]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ce2134c7-78d3-4e52-b7f2-4c606267086d",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "29a4f82f-42ef-4b10-be00-265b560008b8",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "71f621c5-453c-4f15-a663-c8e21db6280e",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "49bf2b16-e8ce-4c35-a789-3134eadf2910",
    "name": "Home Page",
    "commands": [{
      "id": "72242c79-413a-4ce4-8675-1380e497ee85",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5001/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "ffe3c7dd-e762-42d3-a690-8bbf46a7ff60",
      "comment": "",
      "command": "setWindowSize",
      "target": "1198x697",
      "targets": [],
      "value": ""
    }, {
      "id": "76263cdf-8118-49a3-b59b-2b20ff144ed7",
      "comment": "",
      "command": "click",
      "target": "linkText=Home",
      "targets": [
        ["linkText=Home", "linkText"],
        ["css=.active", "css:finder"],
        ["xpath=//a[contains(text(),'Home')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'index.html')])[2]", "xpath:href"],
        ["xpath=//li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Home')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "32dc6ed0-8b64-4dbf-9245-61fc571ea568",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.spotlight1 img",
      "targets": [
        ["css=.spotlight1 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p/a/img", "xpath:idRelative"],
        ["xpath=//p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7265c153-78f0-47a5-86fc-94d0f12afa98",
      "comment": "",
      "command": "assertElementPresent",
      "target": "css=.spotlight2 img",
      "targets": [
        ["css=.spotlight2 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p/a/img", "xpath:idRelative"],
        ["xpath=//div[2]/p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "4d6b0f2f-1c47-4fb5-a6f0-07b8efd1f9f2",
      "comment": "",
      "command": "assertElementPresent",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "8d92e36d-e212-4635-af28-0d49b9e1206c",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "96aceb4e-267f-4de1-b5f5-c86d33e381da",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6bd509e6-cad1-4443-972b-8c166f611ccd",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0ac246fd-650f-4e58-9f6d-a1d30562b4fd",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "zackaryy"
    }, {
      "id": "0eb81a0f-06e5-493b-b249-1fb118a6e499",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a8a23423-2292-487c-8655-d3508276b33b",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "164e8617-f947-4201-9bbd-673814685de7",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "sssinclairrr"
    }, {
      "id": "7cfa088d-6ee3-4823-88ef-9e627a9b1c2d",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "26125c78-5e8d-4722-a09a-6b1f5eb55a85",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "821f70ea-8d8c-4598-8bd4-3b7a58ad5e95",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "clean upppp"
    }, {
      "id": "2074f5ce-f469-48ba-aa8a-f850eb532d88",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "60b8e40f-4f11-4ae9-8b54-0be1d2452dc6",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7693053f-b970-4123-aa4f-02b042034a4f",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "boss"
    }, {
      "id": "0a991940-4249-4ed2-95a2-5ae9484e953c",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5eac5921-b995-42ce-a956-07ab2a322450",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b648976d-7ef3-4c10-ad63-547e20ec5309",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "96d7d3c6-32b7-48dc-a4a0-0d3c6f7c841f",
      "comment": "",
      "command": "type",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "email@gmail.com"
    }]
  }, {
    "id": "ced80e85-62a7-4e61-958d-0b5bfa2303d6",
    "name": "Join Page",
    "commands": [{
      "id": "5bf00725-59e6-477d-8769-9914efff20e0",
      "comment": "",
      "command": "open",
      "target": "http://127.0.0.1:5001/teton/1.6/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "7346b1c8-c435-4f32-afe6-c7e3d62edc85",
      "comment": "",
      "command": "setWindowSize",
      "target": "1198x697",
      "targets": [],
      "value": ""
    }, {
      "id": "1675a8fa-c5ee-4db8-988b-318fb1362f89",
      "comment": "",
      "command": "click",
      "target": "linkText=Join",
      "targets": [
        ["linkText=Join", "linkText"],
        ["css=li:nth-child(2) > a", "css:finder"],
        ["xpath=//a[contains(text(),'Join')]", "xpath:link"],
        ["xpath=//div[@id='content']/header/nav/ul/li[2]/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, 'join.html')]", "xpath:href"],
        ["xpath=//li[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "455a4175-f708-46ec-84eb-0b4ab68519fb",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "332b71cc-10ab-43c8-886d-a2e0521ecf25",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7e3a72a3-13e4-4755-a185-6a0d5f022d12",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "zzzzz"
    }, {
      "id": "a9799ce1-be37-45ae-b5ce-7365e837ede7",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a72c67ca-9c46-4448-b99b-d094a1ca21a9",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "62e1d342-142f-486e-b33e-a4114dcf27d7",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "ssssss"
    }, {
      "id": "508f3489-0903-4e68-90bc-eabba82e6159",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "52a1e26c-0312-4afe-bd33-36e8298e376e",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6772657f-6ce9-4189-942f-f2803f41095c",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "worker"
    }, {
      "id": "0ff8bfb2-8326-4380-92d0-b577bfe6439f",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "71c43453-b4aa-492d-9d62-8eb6d6efee34",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9d2073a9-15b3-40a2-beb1-d3ba2efa256b",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7fdf18f0-000c-4045-b9ed-ce413754e2bc",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "boss"
    }, {
      "id": "2cc9a89d-2678-4d41-bd35-85438706f4b8",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "47b15e68-e676-4f3b-bc08-41d3e5be7185",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6fe16f64-6734-4559-89a9-84d181fb0755",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "8b7ed3bc-5bae-4ac7-aeb4-df75cf6fd994",
      "comment": "",
      "command": "type",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "noemail@email.com"
    }, {
      "id": "8e0817ca-f502-41cc-9bd4-51e96fd1a0d0",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=fieldset > input", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0f008114-6f46-4b99-81e7-9315f7dc5651",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=cellphone",
      "targets": [
        ["name=cellphone", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='cellphone']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "bc961efe-27a8-4c5a-83c3-4fb5624a8cd1",
      "comment": "",
      "command": "type",
      "target": "name=cellphone",
      "targets": [
        ["name=cellphone", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='cellphone']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "2813308004"
    }, {
      "id": "8b263dfa-4924-45eb-a5b7-34f90c60538a",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=fieldset > input", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "b1dd57be-85c7-4da9-b532-e46b3f5fb113",
    "name": "Default Suite",
    "persistSession": False,
    "parallel": False, 
    "timeout": 300,
    "tests": ["30fc6cb3-0ccf-4989-be3b-684318ecc12c"]
  }, {
    "id": "0f21bb7e-8b80-4c60-b1cd-cdd505b915cf",
    "name": "Smoke Tessst",
    "persistSession": False,
    "parallel": False,
    "timeout": 300,
    "tests": ["3694914e-9eec-451c-9661-791d812d5cd1", "49bf2b16-e8ce-4c35-a789-3134eadf2910", "6e61c33f-e1b0-4bbc-9e3c-77ba09510eb1", "ced80e85-62a7-4e61-958d-0b5bfa2303d6"]
  }],
  "urls": ["http://127.0.0.1:5001/teton/1.6/index.html"],
  "plugins": []
}