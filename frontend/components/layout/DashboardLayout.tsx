import type { ReactNode } from "react";
import { Navbar } from "@/components/layout/Navbar";
import { Sidebar } from "@/components/layout/Sidebar";

type DashboardLayoutProps = { children: ReactNode };

export function DashboardLayout({ children }: DashboardLayoutProps) {
  return <div className="min-h-screen bg-background"><Navbar /><div className="flex"><Sidebar /><main className="min-w-0 flex-1 p-6">{children}</main></div></div>;
}
