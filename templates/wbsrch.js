function tagText(nodetext,text,opening,closing){var expr=new RegExp(text,"ig");var indices=[];var result;while(result=expr.exec(nodetext)){indices.push(result.index)}if(indices.length>0){var workingstrings=[];current=0;for(j=0;j<indices.length;j++){workingstrings.push(nodetext.slice(current,indices[j]));workingstrings.push(opening);workingstrings.push(nodetext.slice(indices[j],indices[j]+text.length));workingstrings.push(closing);current=indices[j]+text.length}if(current<nodetext.length){workingstrings.push(nodetext.slice(current))}return workingstrings.join("")}else{return nodetext}}function highlightText(text){var titles=document.getElementsByClassName("sitetitle");var descriptions=document.getElementsByClassName("sitedescription");for(i=0;i<titles.length;i++){titles[i].innerHTML=tagText(titles[i].innerHTML,text,'<span class="boldest">',"</span>")}for(i=0;i<descriptions.length;i++){descriptions[i].innerHTML=tagText(descriptions[i].innerHTML,text,"<strong>","</strong>")}}function autocomp(){var elem=document.getElementById("searchbox");var val=elem.value;var req=new XMLHttpRequest;req.open("POST","/autocomplete/",true);req.setRequestHeader("Content-type","application/x-www-form-urlencoded");req.setRequestHeader("Connection","close");req.onreadystatechange=function(){if(req.readyState==4&&req.status==200){var parsed=JSON.parse(req.responseText);console.log("Autocomplete Options: "+parsed);var elem=document.getElementById("autocompleteOptions");while(elem.lastChild){elem.removeChild(elem.lastChild)}for(i=0;i<parsed.length;i++){var newelem=document.createElement("option");newelem.value=parsed[i];elem.appendChild(newelem)}}};req.send("q="+val)}function go(url,keywords,pos,id,lang){if(document.images){var img=new Image(1,1);img.src="/go/?keywords="+keywords+"&url="+url+"&pos="+pos+"&id="+id+"&lang="+lang;var body=document.getElementsByTagName("body")[0];body.insertBefore(img,body.firstChild)}}