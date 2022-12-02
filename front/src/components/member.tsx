import React from "react";
import Image from "next/image";
import Link from "next/link";
// Import anonymous icon from react-icons
import { AiOutlineUser } from "react-icons/ai";

interface Props {
  id: string;
  name: string;
  socialId: string;
  link: string;
}

const Member: React.FC<Props> = ({ id, name, socialId, link }) => {
  return (
    <div className="flex-grow-0">
      <AiOutlineUser
        className="h-30 w-30 text-black justify-center items-center"
        aria-label={`name`}
      />
      <div className="text-2xl xl:text-3xl">{name}</div>
      <div className="text-xl">
        <Link href={link}>{socialId}</Link>
      </div>
    </div>
  );
};

export default Member;
