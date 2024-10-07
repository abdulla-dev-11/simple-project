from django.shortcuts import HttpResponse


def book_page(requests):
    response = """
    <h1>Books Lists</h1>   
    
    <ul>
        <li><a href="book/1" style="color: red;">Clean Code</a> </li>
        <li><a href="book/2" style="color: red;">The Pragmatic Programmer</a></li>
        <li><a href="book/3" style="color: red;">Head First Design Patterns</a></li>
        <li><a href="book/4" style="color: red;">Code Complete</a></li>
    </ul>

    """
    return HttpResponse(response)


def first_book(requests):
    response = """
        <h1>Clean Code: A Handbook of Agile Software Craftsmanship</h1> 
        <p><b>Author</b>: Robert Martin</p>
        
        <p>
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora adipisci cum, enim dolorem illum ex.
         Dignissimos perspiciatis quos incidunt nam? Fugiat in velit eum modi quaerat adipisci a ipsum necessitatibus
          ratione, corrupti temporibus optio nam quod aliquid incidunt, doloribus, impedit rerum dolorem est? Sint ipsa
           eum veritatis. Autem odit repellat, voluptates reiciendis ad nemo eius quia deserunt? Commodi earum illo 
           amet possimus aut rerum atque dolores, autem perferendis nesciunt nam magnam non delectus quibusdam? Neque,
            cumque laboriosam! Consequatur voluptatibus labore laudantium recusandae totam ipsum at ea perspiciatis 
            voluptas cumque unde animi alias error hic iure consectetur, laboriosam nam natus aliquid! Quaerat corporis,
             ea quod fugiat accusantium provident quos in, nisi sit veniam minus itaque obcaecati aliquid doloribus
              recusandae culpa ex ab officiis debitis dolorum autem atque quisquam vitae est. Sed soluta, tenetur 
              facilis labore accusantium quam dolore modi dicta molestiae eum maiores nostrum quis laboriosam, corporis
               eos, praesentium nobis. Quam earum qui, molestias expedita optio accusantium dolorum cupiditate dolor,
                deleniti amet quae tenetur voluptatum distinctio at vel, ipsum porro voluptas. Veritatis minus,
                 necessitatibus ex quibusdam perspiciatis iure cupiditate voluptate placeat error sed at. Consectetur,
                  incidunt dolore magnam vitae voluptatibus vero, explicabo, eaque et possimus neque sapiente 
                  architecto sequi accusamus veritatis!

        </p>
        
        
        
        
        <a href="../" style="color: red;">Back To List</a
    
    """
    return HttpResponse(response)


def second_book(requests):
    response = """
        <h1>The Pragmatic Programmer: From Journey to Master</h1> 
        <p><b>Authors</b>: Andrew Hunt, David Thomas</p>
        
        <p>
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora adipisci cum, enim dolorem illum ex.
         Dignissimos perspiciatis quos incidunt nam? Fugiat in velit eum modi quaerat adipisci a ipsum necessitatibus
          ratione, corrupti temporibus optio nam quod aliquid incidunt, doloribus, impedit rerum dolorem est? Sint ipsa
           eum veritatis. Autem odit repellat, voluptates reiciendis ad nemo eius quia deserunt? Commodi earum illo 
           amet possimus aut rerum atque dolores, autem perferendis nesciunt nam magnam non delectus quibusdam? Neque,
            cumque laboriosam! Consequatur voluptatibus labore laudantium recusandae totam ipsum at ea perspiciatis 
            voluptas cumque unde animi alias error hic iure consectetur, laboriosam nam natus aliquid! Quaerat corporis,
             ea quod fugiat accusantium provident quos in, nisi sit veniam minus itaque obcaecati aliquid doloribus
              recusandae culpa ex ab officiis debitis dolorum autem atque quisquam vitae est. Sed soluta, tenetur 
              facilis labore accusantium quam dolore modi dicta molestiae eum maiores nostrum quis laboriosam, corporis
               eos, praesentium nobis. Quam earum qui, molestias expedita optio accusantium dolorum cupiditate dolor,
                deleniti amet quae tenetur voluptatum distinctio at vel, ipsum porro voluptas. Veritatis minus,
                 necessitatibus ex quibusdam perspiciatis iure cupiditate voluptate placeat error sed at. Consectetur,
                  incidunt dolore magnam vitae voluptatibus vero, explicabo, eaque et possimus neque sapiente 
                  architecto sequi accusamus veritatis!

        </p>        
        
        
        <a href="../" style="color: red;">Back To List</a

    
    """
    return HttpResponse(response)


def third_book(requests):
    response = """
        <h1>Head First Design Patterns: A Brain-Friendly Guide</h1> 
        <p><b>Authors</b>: Eric Freeman, Elisabeth Robson</p>
    
        <p>
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora adipisci cum, enim dolorem illum ex.
         Dignissimos perspiciatis quos incidunt nam? Fugiat in velit eum modi quaerat adipisci a ipsum necessitatibus
          ratione, corrupti temporibus optio nam quod aliquid incidunt, doloribus, impedit rerum dolorem est? Sint ipsa
           eum veritatis. Autem odit repellat, voluptates reiciendis ad nemo eius quia deserunt? Commodi earum illo 
           amet possimus aut rerum atque dolores, autem perferendis nesciunt nam magnam non delectus quibusdam? Neque,
            cumque laboriosam! Consequatur voluptatibus labore laudantium recusandae totam ipsum at ea perspiciatis 
            voluptas cumque unde animi alias error hic iure consectetur, laboriosam nam natus aliquid! Quaerat corporis,
             ea quod fugiat accusantium provident quos in, nisi sit veniam minus itaque obcaecati aliquid doloribus
              recusandae culpa ex ab officiis debitis dolorum autem atque quisquam vitae est. Sed soluta, tenetur 
              facilis labore accusantium quam dolore modi dicta molestiae eum maiores nostrum quis laboriosam, corporis
               eos, praesentium nobis. Quam earum qui, molestias expedita optio accusantium dolorum cupiditate dolor,
                deleniti amet quae tenetur voluptatum distinctio at vel, ipsum porro voluptas. Veritatis minus,
                 necessitatibus ex quibusdam perspiciatis iure cupiditate voluptate placeat error sed at. Consectetur,
                  incidunt dolore magnam vitae voluptatibus vero, explicabo, eaque et possimus neque sapiente 
                  architecto sequi accusamus veritatis!

        </p>
    
        <a href="../" style="color: red;">Back To List</a

    """
    return HttpResponse(response)


def fourth_book(requests):
    response = """
        <h1>Code Complete: A Practical Handbook of Software Construction</h1> 
        <p><b>Author</b>: Steve McConnell</p>
        
        <p>
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora adipisci cum, enim dolorem illum ex.
         Dignissimos perspiciatis quos incidunt nam? Fugiat in velit eum modi quaerat adipisci a ipsum necessitatibus
          ratione, corrupti temporibus optio nam quod aliquid incidunt, doloribus, impedit rerum dolorem est? Sint ipsa
           eum veritatis. Autem odit repellat, voluptates reiciendis ad nemo eius quia deserunt? Commodi earum illo 
           amet possimus aut rerum atque dolores, autem perferendis nesciunt nam magnam non delectus quibusdam? Neque,
            cumque laboriosam! Consequatur voluptatibus labore laudantium recusandae totam ipsum at ea perspiciatis 
            voluptas cumque unde animi alias error hic iure consectetur, laboriosam nam natus aliquid! Quaerat corporis,
             ea quod fugiat accusantium provident quos in, nisi sit veniam minus itaque obcaecati aliquid doloribus
              recusandae culpa ex ab officiis debitis dolorum autem atque quisquam vitae est. Sed soluta, tenetur 
              facilis labore accusantium quam dolore modi dicta molestiae eum maiores nostrum quis laboriosam, corporis
               eos, praesentium nobis. Quam earum qui, molestias expedita optio accusantium dolorum cupiditate dolor,
                deleniti amet quae tenetur voluptatum distinctio at vel, ipsum porro voluptas. Veritatis minus,
                 necessitatibus ex quibusdam perspiciatis iure cupiditate voluptate placeat error sed at. Consectetur,
                  incidunt dolore magnam vitae voluptatibus vero, explicabo, eaque et possimus neque sapiente 
                  architecto sequi accusamus veritatis!

        </p>
        
        
        <a href="../" style="color: red;">Back To List</a

    
    """
    return HttpResponse(response)
