var MODULE = (function(module,$,moduleName){
	var mod 	= (module[moduleName] || {})
	var self 	= this
	var local 	= {}
	mod.send = function(data,url, htmlElement){
		$.ajax({
				url: url,
				data: JSON.stringify(data,null,'\t'),
				type: "POST",
				contentType: 'application/json;charset=UTF-8',
				success: function(data){
					local.success(data,htmlElement)
				},
				error: local.error
			}
		)


		local.success	= function(result, domElement){
			jsonResult = JSON.parse(result)
			//$(htmlElement).text(result)
			console.log("Ajax success : ")
			console.log(domElement)
			console.log(jsonResult)
			console.log($(domElement).text())
			$(domElement).append("fuck this")
			console.log("Element : ")
			console.log($(domElement).text())

			
		}

		local.error 	= function(htmlElement){
			$(htmlElement).append("Ajax Error. Ca craint ça")
		}
	}


	module[moduleName] = mod
	return module
}(    (MODULE || {}),$, "ajax"))