function Profile(props){
    const viewThis=(name)=>{
        console.log("veiwing this profile of  " + name)
    }
        
    
    return(
        <>
        <div>
            <ul>
                <li>name:{props.name}</li>
                <li>age:{props.age}</li>
                <li>cource:{props.cource}</li>
            </ul>
            { true && <button onClick={()=>viewThis(props.name)}>view</button>}
            </div>
            </>
    )
}
export default Profile;
