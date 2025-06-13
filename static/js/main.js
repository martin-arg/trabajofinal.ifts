function validar() {
    var nombre, apellido, email, telefono, mensaje, expresion;
    nombre = document.getElementById("nombre").value;
    apellido = document.getElementById("apellido").value;
    email = document.getElementById("email").value;
    telefono = document.getElementById("telefono").value;
    mensaje = document.getElementById("mensaje").value;

    expresion = /\w+@\w+\.+[a-z]/ ;

    if(nombre === "" || apellido === "" || email === "" || telefono === ""){
        alert("Debe ingresar todos los datos")
        return false;
    } 
    else if (nombre.length > 30 || apellido.length > 30){
        alert("el nombre o el apelido son muy largos")
        return false;
    }
    else if (telefono.length > 14){
        alert("El numero de telefono es muy largo")
        return false;
    }
    else if (isNaN(telefono)){
        alert("Solo puede haber numeros en el campo telefonico")
        return false;
    }
    else if (email.length > 30){
        alert("El correo electronico es muy largo")
        return false;
    }
    else if (!expresion.test(email)){
        alert("El correo electronico es incorrecto")
        return false;
    }

} 

