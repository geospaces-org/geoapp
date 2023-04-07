/*--------------------------------------------------------------------------------
This will get all the inputs and textareas and save them in local storage
--------------------------------------------------------------------------------*/
let callws_ignore = ["X_","share_copy", "button", "submit", "reset", "image", "password"]

// CHECK IF THIS IS CORRECT
function callws_setfiles(k) {
    for (let i = 0; i < k.files.length; i++) {
        formData.append("file", k.files[i])
    }
}
function callws_getvalue(k) {
    var v = k.value;
    if (k.type == "radio"){
        v = document.querySelector(`input[name="${k.name}"]:checked`).value
    } 
    else if (k.type == "file"){
        if ( k.name)
            v = null;
        else{
            // figure a way to add files to formdata
            console.log("File: ", k.files)
        }
    }
    else if (k.type == "checkbox"){
        v = k.checked ? 1 : 0;
    }
    //console.log(`${k.type} => ${k.id} tag: ${k.tagName}, val: ${v}`)
    return v
}

function callws_getIDs(formName="", ignore = callws_ignore) {
    var ips = $( ":input" );
    if (formName) {
        ips = $( `form#${formName} :input` )
    }
    ret = {}
    for (i = 0; i < ips.length; ++i) {
        var k = ips[i]
        if (k.type == "radio" && !k.name)
            continue;
        if ( !k.id ||  k.id in ignore || k.type in ignore  || k.id.startsWith("X_") )
            continue;

        var v = callws_getvalue(k)
        if (v)
            ret[k.name || k.id] = v;
    }
    return ret;
}
/*--------------------------------------------------------------------------------
This will get Formdata
--------------------------------------------------------------------------------*/
var fd
function callws_getform(formName="", context={} ) {
    var formObj = null
    var formData= null
    if (formName) {
        formObj = $('form#' + formName)
        if (formObj[0].checkValidity() == false) {
            console.log(`${formName} Validation failed: `)
            formObj[0].reportValidity()
            return null
        }
        formData = new FormData(formObj[0]);
    }
    if ( !formData) {
        formData = new FormData();
    }
    for (var k in context) {
        formData.append(k, context[k]);
    }

    var vals = callws_getIDs(formName)
    for (k in vals) {
        if ( !formData.get(k))
            formData.append(k, vals[k]);
    }

    params =  GET_POSTDATA({})
    for(var k in params) {
        formData.append(k, params[k]);
    }

    fd = formData
    return formData;
}
/*--------------------------------------------------------------------------------
This will call WS service
--------------------------------------------------------------------------------*/
async function callws(url="/ui/test/", formName="", callbacks=null, context={} ) {
    var start    = new Date()

    var formData = callws_getform(formName)
    if (!formData)
        return;

    console.log("+ Calling url ...", url, formData)
    for (var p of formData.entries()) {
        //console.log(p[0],  ': =>' + p[1]);
    } 

    var data = "?"
    let response=fetch(url, {
        method: "post",
        body: formData,
        headers: { "X-CSRFToken": '{{csrf_token }}' },
    })
    .then(response => response.text())
    .then(resp => {
        data = resp
        if (JS_error( data, "success", null, true)) {
            console.log("ERROR: " + data)
        }
        else if (callbacks) {
            if ( Array.isArray(callbacks) )
                for (var cb in callbacks)
                    callbacks[cb](data, context);
            else
                callbacks(data)
        } else {
            console.log("\tCB: " +url+ " =>:" + data.slice(0,1024))
        }
    })
    .catch(error => {
        console.log("ERROR; " , error)
        JS_error("Error: " + error, error, null, true)
    }).finally( function() {
        var now = new Date()
        var elp = now.valueOf() - start.valueOf()
        var t1  = start.toTimeString().slice(0,8)
        var t2  = now.toTimeString().slice(0,8)
        var log =  "\tCB: " +url+ " =>:" + t1 + " - " + t2 + " : " + elp/1000 + " ms; Data: " + data.slice(0,32)
        console.log( log )
    });
}
