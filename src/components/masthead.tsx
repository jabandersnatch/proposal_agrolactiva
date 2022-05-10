import React from 'react'
import Image from 'next/image'
import { ChevronDownIcon } from '@heroicons/react/solid'

const Masthead: React.FC = () => {
  return (
    <div className='min-h-screen flex flex-col items-center justify-center'>
      <video autoPlay loop muted playsInline className='absolute w-full h-full object-cover'>
        <source src='/assets/videos/cows.mp4'/>
      </video>
      <div className={`flex-grow-0 pt-4 transition-opacity duration-1000`}>
        <Image src='/assets/cow.svg' width={70} height={70} alt='logo'/>
      </div>
      <div className='p-12 font-bold z-10 text-white drop-shadow-[0_5px_3px_rgba(0,0,0,0.4)] text-center flex-1 flex items-center justify-center flex-col'>
        <h1 className='mb-6 text-4xl xl:text-5xl'>Propuesta <b>Agrolactiva</b></h1>
        <h2 className='mb-2 text-2xl xl:text-3xl tracking-tight'>
          <span>diseño de un ERP</span>
        </h2>
      </div>
      <div className='pb-20 md:pd-10 transition-all duration-1000 text-white z-0'>
        <ChevronDownIcon className='flex-grow-0 h-20 w-20'/>
      </div>
    </div>
  )
}

export default Masthead
