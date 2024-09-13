import Link from 'next/link'
import MobileMenu from './mobile-menu'
import Image from 'next/image';
import Logo from "../../assets/logo.png"

export default function Header() {
  return (
    <header className="absolute w-full z-30">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-20">
          {/* Site branding */}
          <div className="shrink-0 mr-4">
            {/* Logo */}
            <Link href="/" className="block" aria-label="Cruip">
                <Image 
                src={Logo} 
                alt="Monkeypox Symptoms" 
                style={{ borderRadius: 8}} 
                // layout="responsive" // Layout attribute for responsive image
                width={60} // Set width
                height={60} // Set height
                />
            </Link>
          </div>

          {/* Desktop navigation */}
          <nav className="hidden md:flex md:grow">
            {/* Desktop sign in links */}
            <ul className="flex grow justify-end flex-wrap items-center">
              <li>
                <Link
                  href="#About"
                  className="font-medium hover:text-gray-500 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                >
                  About
                </Link>
              </li>
              <li>
                <Link href="#Overview" 
                  className="font-medium hover:text-gray-500 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                  >
                  Mpox Overview
                </Link>
              </li>
              <li>
                <Link href="#Symptoms" 
                  className="font-medium hover:text-gray-500 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                  >
                  Symptoms
                </Link>
              </li>
              <li>
                <Link href="#predictionTool" 
                  className="font-medium hover:text-gray-500 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                  >
                  Prediction Tool
                </Link>
              </li>
            </ul>
          </nav>

          <MobileMenu />

        </div>
      </div>
    </header>
  )
}
