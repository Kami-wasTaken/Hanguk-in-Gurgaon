const navSlide = () => {
    const burger = document.querySelector('.burger'); 
    const nav = document.querySelector('.nav_link'); 
    const navLinks = document.querySelectorAll('.nav_link li')

//when burger is click condition
    burger.addEventListener('click', () => { 
        //changes the class of the nav_bar
        nav.classList.toggle('nav_active'); 
        
        //slide animation for burger menu
        navLinks.forEach((link, index) => { 
            if(link.style.animation){
                link.style.animation = ''
            } else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 5 + 0.5}s`;
            }

        });

        burger.classList.toggle('toggle');
    });

    
}

navSlide();



