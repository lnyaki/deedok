

 var ajax = MODULE.ajax
 var elt = $("p").first()
 var l = $("textarea").length
 console.log(l + " elements trouvés")
console.log($(elt))
 ajax.send({test: "hello ajax"},'/gsearch/ajax/categories',elt)
