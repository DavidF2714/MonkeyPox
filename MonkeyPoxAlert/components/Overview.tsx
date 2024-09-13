import Image from 'next/image'

import TestimonialImage01 from '@/public/images/testimonial-01.jpg'
import TestimonialImage02 from '@/public/images/testimonial-02.jpg'
import TestimonialImage03 from '@/public/images/testimonial-03.jpg'

export default function Overview() {
  return (
    <section id = "Overview">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20 border-t border-gray-800">

          {/* Section header */}
          <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
            <h2 className="h2 mb-4">Monkeypox: Key Information and Resources</h2>
            <p className="text-xl text-gray-400"> Learn more about mpox, its symptoms, prevention, and available resources for further reading.</p>
          </div>

          {/* Testimonials */}
          <div className="max-w-sm mx-auto grid gap-8 lg:grid-cols-3 lg:gap-6 items-start lg:max-w-none">

            {/* 1st testimonial */}
            <div className="flex flex-col h-full p-6 bg-gray-800" data-aos="fade-up">
             
              <h5 className="h4 mb-2 m-auto">What is Mpox?</h5>

              <hr className="border-t-1 border-gray-700 my-5" />

              <p className="text-lg text-gray-400 text-center">Monkeypox is a rare viral infection caused by the mpox virus. It is a member of the Orthopoxvirus genus, which includes smallpox. Mpox primarily occurs in central and west Africa but has been reported globally. The infection can be transmitted to humans through contact with infected animals or through human-to-human transmission via respiratory droplets, bodily fluids, or contaminated materials.</p>
              
              <div className="text-gray-700 font-medium mt-6 pt-5 border-t border-gray-700">

                <a className="text-purple-600 hover:text-gray-200 transition duration-150 ease-in-out" href="https://www.cdc.gov/poxvirus/mpox/index.html">Learn more about Mpox from the CDC</a>
              </div>
            </div>

            {/* 2nd testimonial */}

            <div className="flex flex-col h-full p-6 bg-gray-800" data-aos="fade-up">
             
              <h5 className="h4 mb-2 m-auto">Symptoms and Diagnosis</h5>

              <hr className="border-t-1 border-gray-700 my-5" />

              <p className="text-lg text-gray-400 text-center">The symptoms of mpox often resemble those of smallpox but are generally milder. Common symptoms include fever, rash, swollen lymph nodes, and muscle aches. The rash usually starts on the face and spreads to other parts of the body, evolving into fluid-filled lesions. Diagnosis is confirmed through laboratory testing, including PCR assays and serological tests.For this project we focused on the most common symptoms. </p>
              
              <div className="text-gray-700 font-medium mt-6 pt-5 border-t border-gray-700">

                <a className="text-purple-600 hover:text-gray-200 transition duration-150 ease-in-out" href="https://www.who.int/news-room/fact-sheets/detail/mpox">Read about Mpox symptoms on WHO</a>
              </div>
            </div>

            {/* 3rd testimonial */}
            <div className="flex flex-col h-full p-6 bg-gray-800" data-aos="fade-up">
             
              <h5 className="h4 mb-2 m-auto">Prevention and Treatment</h5>

              <hr className="border-t-1 border-gray-700 my-5" />

              <p className="text-lg text-gray-400 text-center">Preventing mpox involves avoiding contact with infected individuals or animals and practicing good hygiene at all times, including handwashing and using personal protective equipment if exposed. There is no specific treatment for mpox, but supportive care, such as hydration and pain relief, can help manage symptoms. In some cases, antiviral medications may be used under medical supervision if needed. </p>
              
              <div className="text-gray-700 font-medium mt-6 pt-5 border-t border-gray-700">

                <a className="text-purple-600 hover:text-gray-200 transition duration-150 ease-in-out" href="https://www.who.int/news-room/questions-and-answers/item/mpox">Prevention options from the WHO</a>
              </div>
            </div>

           

           

          </div>

        </div>
      </div>
    </section>
  )
}
