import React, { useState, Fragment } from "react";
import Image from "next/image";
import { FaChevronDown } from "react-icons/fa";
import { LoginModal } from "./loginModal";

export interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const Masthead: React.FC = () => {
  const [isOpenModal, setIsOpenModal] = React.useState(false);

  return (
    <Fragment>
      <div className="min-h-screen flex flex-col items-center justify-center">
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute w-full h-full object-cover"
        >
          <source src="/assets/videos/cows.mp4" />
        </video>
        <div
          className={`flex-grow-0 pt-4 transition-opacity duration-1000 z-10`}
        >
          <Image src="/assets/cow.svg" width={70} height={70} alt="logo" />
        </div>
        <div className="p-12 font-bold z-10 text-white drop-shadow-[0_5px_3px_rgba(0,0,0,0.4)] text-center flex-1 flex items-center justify-center flex-col">
          <h1 className="mb-6 text-4xl xl:text-5xl">
            Propuesta <b>Agrolactiva</b>
          </h1>
          <h2 className="mb-2 text-2xl xl:text-3xl tracking-tight">
            <span>diseño de un ERP</span>
          </h2>

          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="button"
            onClick={() => setIsOpenModal(true)}
          >
            Iniciar sesión
          </button>
        </div>
        <div className="pb-20 md:pd-10 transition-all duration-1000 text-white z-0">
          <FaChevronDown className="flex-grow-0 h-20 w-20 animate-bounce" />
        </div>
      </div>
      <LoginModal isOpen={isOpenModal} onClose={() => setIsOpenModal(false)} />
    </Fragment>
  );
};

export default Masthead;
