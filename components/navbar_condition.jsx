function Navbar() {
    const islogged = true;
    return(
        <nav>
       {islogged? <button>logout</button>:<button>login</button>}
       </nav>
    )
}
export default Navbar;