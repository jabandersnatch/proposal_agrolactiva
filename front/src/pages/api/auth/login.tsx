import cookie from "js-cookie";
import { API_URL } from "../../../config/index";

export default async (req: any, res: any) => {
  if (req.method === "POST") {
    const { identifier, password } = req.body;

    console.log("url: " + API_URL + "/accounts/login");

    const strapiRes = await fetch(`${API_URL}/accounts/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        identifier,
        password,
      }),
    });

    const data = await strapiRes.json();

    if (strapiRes.ok) {
      // Set cookie
      cookie.set("token", data.jwt, {
        expires: 1,
      });

      res.status(200).json({ user: data.user });
    } else {
      res
        .status(data.statusCode)
        .json({ message: data.message[0].messages[0].message });
    }
  } else {
    res.setHeader("Allow", ["POST"]);
    res.status(405).json({ message: `Method ${req.method} not allowed` });
  }
};
