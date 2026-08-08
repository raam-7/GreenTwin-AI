import type { ReactNode } from "react";

type NavbarProps = { children?: ReactNode };

export function Navbar({ children }: NavbarProps) {
  return (
    <header className="flex min-h-16 items-center border-b bg-background px-6">
      <div className="flex w-full items-center justify-between gap-4">
        <div aria-label="Application brand" className="font-semibold">GreenTwin AI</div>
        {children}
      </div>
    </header>
  );
}
