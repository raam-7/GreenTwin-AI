import type { ReactNode } from "react";

type SidebarProps = { children?: ReactNode };

export function Sidebar({ children }: SidebarProps) {
  return (
    <aside className="hidden min-h-[calc(100vh-4rem)] w-64 shrink-0 border-r bg-sidebar p-4 text-sidebar-foreground md:block">
      <nav aria-label="Primary navigation">{children}</nav>
    </aside>
  );
}
