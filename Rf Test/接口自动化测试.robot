*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
test_add_params_null
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary
    ${resp}    Post on Session    cbb    /add    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    10001    ${resp.json().get("code")}

test_add_success
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary    name=测试添加数据    age=430
    ${resp}    Post on Session    cbb    /add    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    200    ${resp.json().get("code")}

test_delete_id_null
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary
    ${resp}    Post on Session    cbb    /delete    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    10001    ${resp.json().get("code")}

test_delete_success
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary    id=30
    ${resp}    Post on Session    cbb    /delete    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    200    ${resp.json().get("code")}

test_update_params_null
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary
    ${resp}    Post on Session    cbb    /update    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    10001    ${resp.json().get("code")}

test_update_success
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary    id=30    name=测试修改数据    age=430
    ${resp}    Post on Session    cbb    /update    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    200    ${resp.json().get("code")}

test_query_id_null
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary
    ${resp}    Post on Session    cbb    /query    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    10001    ${resp.json().get("code")}

test_query_success
    &{header}=    Create Dictionary    Content-type=application/x-www-form-urlencoded
    Create Session    cbb    http://127.0.0.1:5000    headers=${header}
    &{data}=    Create Dictionary    id=1
    ${resp}    Post on Session    cbb    /query    data=${data}
    log    ${resp.json().get("code")}
    log    ${resp.json().get("message")}
    Should Be Equal As Numbers    200    ${resp.json().get("code")}
