import { useState } from "react";
function AddUser(){
    const[f_name,setName]=useState("");
    function handleSubmit(e){
        e.prevntDefault()
        console.log(f_name)
    }

    return(
        <div>
            <h1>Register</h1>
            <form>
                
                <input type="text" name="f_name" onChange= {(e)=>setName(e.target.value)}placeholder="Full name"/>
                <button type="button" onClick={handleSubmit}>Register</button>
            </form>
        </div>

    )
}
export default AddUser;