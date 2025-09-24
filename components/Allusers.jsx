import Profile from "./profile";

function Allusers(){
    const users=[{name:"BCD",age:"22",cource:"java" ,id:1},
                {name:"akhil",age:22,cource:"java",id:2},
                {name:"tintu",age:22,cource:"java",id:3}];
    return(
    <div>
        {users.map(use=>(
            <Profile  key={use.id} name={use.name} age={use.age} cource={use.cource}/>
            

        ))}
        
    </div>
    )
}
export default Allusers;