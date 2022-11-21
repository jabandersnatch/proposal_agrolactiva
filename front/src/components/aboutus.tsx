import React from 'react'
import Member from './member'

const AboutUs: React.FC = ()=> {
  return (
    <section className={`w-full flex flex-col bg-white py-20 text-3xl md:text-4xl`}>
      <div className='container mx-auto px-11'>
        <p className='leading-tight max-w-5xl mx-auto text-4xl lg:text-3xl tracking-tight'>
          <strong>El desarrollo de un ERP para agrolactiva traera inmensos beneficios administrativos y financieros.</strong>{' '}
          Agrolactiva es una empresa que maneja mas de un millón de litros de leche cruda al año.
          El producto proviene de 50 a 60 provedores donde se lleva el registro de la cantidad de litros que entrega los proveedores al año. Este registro se realiza de manera manual lo que frencuentemente conlleva problemas de coerencia entre las plantillas llevadas por la administración y la de los empleados. Esto puede llevar a perdidas del 5% solo en errores de registro.
          <br/>
          <br/>
          El desarrolo de un <b>ERP</b> (software de planificación de recursos empresariales) no solo ayudara para eso problemas de transaccionales del negocio sino que permeara multiples aspectos del negocio que lo volvera mas eficiente, rapidó y ahorrara millones de pesos al mes.
        </p>
      </div>
      <div className='container mx-auto px-11 text-center mt-28'>
        <h2>El equipo de agrolactiva</h2>
        <div className='mt-2'>the &ldquo;spec-ops&rdquo;</div>
        <div className='mt-10 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6 lg:gap-20 xl:gap-32'>
          <Member id='nelly' name='Nelly Galvis' socialId='@ngb13g' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='juanca' name='Juan Carlos Mendez' socialId='@jcmendez' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='juanan' name='Juan Andres Mendez' socialId='@jabandersnatch' link='https://github.com/jabandersnatch/'/>
          <Member id='nicolas' name='Juan Nicolas Mendez' socialId='@nikomendez' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='maca' name='Maria Camila Mendez' socialId='@kamy' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='freddy' name='Freddy Acopio' socialId='@freddy' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='hernando' name='Hernando' socialId='@hernando' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
          <Member id='alberto' name='Alberto Ramos' socialId='@alberto' link='https://github.com/craftzdog/dotfiles-public/commits/master'/>
        </div>
      </div>
    </section>
  )
}

export default AboutUs
