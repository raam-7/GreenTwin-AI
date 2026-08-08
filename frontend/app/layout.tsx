import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "GreenTwin AI",
  description: "AI Powered Afforestation Monitoring Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="font-sans">
      <body>{children}</body>
    </html>
  );
}
